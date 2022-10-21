from flask import Flask,jsonify,request
import csv

allarticles=[]
likedarticles=[]
dislikedarticles=[]
notwatchedarticles=[]

with open('article.csv',encoding='utf-8') as x:
    reader=csv.reader(x)
    data=list(reader)
    allarticles=data[1:]

app=Flask(__name__)
@app.route('/get-article')

def getarticle():
    return jsonify({
        'data': allarticles[0]
    })

@app.route('/liked-article', methods=['POST'])
def likearticle():
    article=allarticles[0]
    likedarticles.append(article)
    allarticles=allarticles[1:]
    return jsonify({
        'status':'succes'
    })

@app.route('/disliked-article',methods=['POST'])
def dislikedarticle():
    article=allarticles[0]
    dislikedarticles.append(article)
    allarticles=allarticles[1:]
    return jsonify({
        'status':'succes'
    })

@app.route('/notwatchedarticle',methods=['POST'])
def notwatchedarticle():
    article=allarticle[0]
    notwatchedarticle.append(article)
    allarticle=allarticle[1:]
    return jsonify({
        'status':'succes'
    })
app.run()
