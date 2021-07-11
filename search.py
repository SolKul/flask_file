import pandas as pd
import re,io

def search(text,keywords_file):
    # werkzeug.datastructures.FileStorageをデータフレームに変換
    keyword_df=pd.read_excel(keywords_file)
    # キーワードを取得
    keywords=keyword_df.columns.tolist()
    results=[]
    for keyword in keywords:
        # テキスト中に含まれるキーワード数を数える
        match_num=len(re.findall(keyword,text))
        # resultsに追加
        results.append(str(match_num))

    nos=range(len(results))
    result_df=pd.DataFrame([results],columns=keywords)

    # https://stackoverflow.com/questions/35710361/python-flask-send-file-stringio-blank-files
    proxy = io.StringIO()
    result_df.to_csv(proxy, index=False)
    
    # Creating the byteIO object from the StringIO Object
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode())
    # seeking was necessary. Python 3.5.2, Flask 0.12.2
    mem.seek(0)
    proxy.close()

    return results,keywords,nos,mem