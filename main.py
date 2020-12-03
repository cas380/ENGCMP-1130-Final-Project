import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def root():
	# use render_template to convert the template code to HTML.
	# this function will look in the templates/ folder for your file.
	return flask.render_template('index.html', page_title='Main Page')

@app.route('/exhibits')
@app.route('/exhibits.html')
def museum():
	video_map = {
		"https://www.youtube.com/embed/SJF4gl2k9Hs": ["The End is Nigh!", "This project was for the Minicast..."],
		"https://www.youtube.com/embed/_ZRU6ovWhHM": ["The Return", "This project was for the Essay Film..."],
	}
	return flask.render_template('exhibits.html', page_title='THE MUSEMU', videos=video_map)


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
