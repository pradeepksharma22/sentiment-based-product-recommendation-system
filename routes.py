
from app import app
from flask import request, render_template
from model import SentimentRecommenderModel
import json

sentiment_model = SentimentRecommenderModel()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def prediction():
    # get user from the html form
    user = request.form['userName']
    # convert text to lowercase
    user = user.lower()
    items = sentiment_model.getSentimentRecommendations(user)

    if(not(items is None)):
        print(f"retrieving items....{len(items)}")
        print(items)
        return render_template("index.html", column_names=items.columns.values, row_data=list(items.values.tolist()), zip=zip)
    else:
        return render_template("index.html", message="User Name doesn't exists, No product recommendations at this point of time!")


@app.route('/predict_sentiment')
def predict_sentiment():
    # get review text from the html form
   # review_text = request.form["reviewText"]
    review_text = request.args.get('review_text')

    print(review_text)
    pred_sentiment = sentiment_model.classify_sentiment(review_text)
    print(pred_sentiment)
    return json.dumps(pred_sentiment[0], default=str)
    #return render_template("index.html", sentiment=pred_sentiment)