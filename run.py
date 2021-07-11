from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file)
import search

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def upload():
    # werkzeug.datastructures.FileStorageを取得
    file = request.files['searched']
    # read()でバイトデータを取得
    text_byte=file.read()
    # バイナリデータをutf-8に変換
    text=text_byte.decode('utf-8')

    # keywordエクセルを取得
    keywords_file = request.files['keywords']
    # 
    results,keywords,nos,mem=search.search(text,keywords_file)

    # render_template(
    #         'uploaded.html',
    #         keywords=keywords,
    #         results=results,
    #         nos=nos)

    return send_file(
        mem,
        attachment_filename="result.txt",
        as_attachment=True)

if __name__ == "__main__":
    app.run()