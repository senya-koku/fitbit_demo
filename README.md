
tcx2df.py：

fitbit内のアクティビティ記録から取得できるtcxファイルをpandasのDataFrameに変換する

[example]

```
import tcx2df
path_tcx_file = 'xxx.tcx'
#tcxファイルに対する前処理と読み込み
xml_data = tcx2df.tcx_file_convert(path_tcx_file)
df = tcx2df.xml2df(xml_data)
df = tcx2df.pp_data(df)
```
