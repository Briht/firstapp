from flask import Flask, render_template
import feedparser


app = Flask(__name__)
BBC_FEED = {
			"bbc": "http://feeds.bbci.co.uk/news/rss.xml",
			"cnn": "http://rss.cnn.com/rss/edition.rss",
			"foxnews": "http://feeds.foxnews.com/foxnews/latest",
			}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
	feed = feedparser.parse(BBC_FEED[publication])

	return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
	app.run(port=5000, debug=True)
