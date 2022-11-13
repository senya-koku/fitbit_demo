
tcx2df.py：

fitbit内のアクティビティ記録から取得できるtcxファイルをpandasのDataFrameに変換する

<example>

```
import tcx2df

path_tcx_file = 'xxx.tcx'
#tcxファイルに対する前処理と読み込み
path_new = tcx2df.tcx_file_convert(path_tcx_file)
xml_data = open(path_new).read()
df = tcx2df.xml2df(xml_data)
df = tcx2df.pp_data(df)
```
