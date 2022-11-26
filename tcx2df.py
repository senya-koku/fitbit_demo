import pandas as pd
import xml.etree.ElementTree as ET


def remove_unnecessary_attribute(lines):
    #xmlファイルとして読み込むときに邪魔になるattributeを除去
    for i in range(len(lines)):
        try:
            if 'Position' in lines[i] or 'HeartRateBpm' in lines[i] or 'Lap' in lines[i]:
                lines.pop(i)
        except IndexError:
            None
            #print('IndexError')
    return lines


def tcx_file_convert(path_tcx_file):
    #tcxファイルをxmlファイルとして読み込めるように前処理を行う
    with open(path_tcx_file) as f:
        lines = f.readlines()
        first = []
    first.append(lines[0])
    new_lines = first + lines[11:-8]
    new_lines = remove_unnecessary_attribute(new_lines)
    return "".join(new_lines)


def xml2df(xml_data):
    root = ET.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    df = pd.DataFrame(all_records)
    return df


def pp_data(df):
    df['Time'] = pd.to_datetime(df['Time'].apply(lambda x: x[:-6]))
    df['Latitude'] = df['LatitudeDegrees'].astype('float')
    df['Longitude'] = df['LongitudeDegrees'].astype('float')
    df['Altitude'] = df['AltitudeMeters'].astype('float')
    df['Distance'] = df['DistanceMeters'].astype('float')
    df['HeartRate'] = df['Value'].astype('float')
    return df.drop(['LatitudeDegrees', 'LongitudeDegrees', 'AltitudeMeters', 'DistanceMeters', 'Value'], axis=1)