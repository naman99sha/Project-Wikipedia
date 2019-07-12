from flask import Flask,render_template,redirect,session,request,abort
import wikipedia_vips
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('main.html')
@app.route('/search',methods=['POST','GET'])
def search():
    try:
        if request.method=='POST':
            key=str(request.form['nm'])
            pg=wikipedia_vips.page(key)
            content=pg.content
            content=content.encode('unicode-escape').decode('utf-8')
            title=pg.title
            title=title.encode('unicode-escape').decode('utf-8')
            summ=wikipedia_vips.summary(key)
            summ=summ.encode('unicode-escape').decode('utf-8')
            return render_template('index.html',content=content,title=title,summ=summ)
        else:
            return render_template('main.html')
    except:
        return "Page related to the entered Keyword not found"
if __name__=='__main__':
    app.run(debug=True)
 ##@app.route('/search',methods=['POST','GET'])   
