from flask import Flask, jsonify, request
import csv

allArticles = []

with open("articles.csv", encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]

likedArticles = []
unlikedArticles = []

app = Flask(__name__)

@app.route('/getData')
def getArticleData():
    return jsonify({
        "data": allArticles[0],
        "status": "Success"
    }, 400)


@app.route('/getLikedData', methods=['POST'])
def getLikedMovies(allArticles=allArticles):
    article = allArticles[0]
    allArticles = allArticles[1:]
    likedArticles.append(article)
    return jsonify({
        "status": "Success" 
    }), 400 
    
@app.route('/getUnlikedData', methods=['POST'])
def getUnlikedMovies(allArticles=allArticles):
    article = allArticles[0]
    allArticles = allArticles[1:]
    unlikedArticles.append(article)
    return jsonify({
        "status": "Success" 
    }), 400 


if __name__ == '__main__':
    app.run()