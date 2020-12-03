import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def root():
	return flask.render_template('index.html', page_title='Main Page')

@app.route('/exhibits')
@app.route('/exhibits.html')
def museum():
	video_map = {
		"-O2pFd_ClTY": ["Narnia State Constitution Project", "This was my first big video project. It was made for the State Constitution Project in my 9th grade civics class."],
		"h9l4QsT2zxs": ["Stuttgart Attractions", "This was my first time using a greenscreen. This project was made for my 10th grade German class to suggest vacation destinations to the teacher's friend."],
		"jywTa7M09Iw": ["Idiot's Guide to Russia Under Peter the Great", "This project was made for an 11th grade Russian History seminar."],
		"FYMsJqgKRVI": ["Cooking with Carter (S1E2): Bartleby's Omelette", "This project was made for a 12th grade English assignment. It's not actually the second episode, that's just branding."],
		"dic16VrTIEI": ["Group Storytelling: Phillip II and Elizabeth I", "This project was made for a 12th grade Western Civ II assignment."],
		"bDYI3WQvziI": ["NYG Beforehand Promo", "This project wasn't made for school, but it's definitely noteworthy. It was made to advertise the National Youth Gathering to the congregation."],
		"k7_LgEGGTwo": ["Interview Podcast", "This podcast was made for a project in ENGCMP 610 in sophomore year."],
		"nVr6fX_cwaA": ["Star Wars: Episode XV - Thanksgiving Break", "This project is my magnum opus. It was made as my final project for ENGCMP 610 in sophomore year."],
		"SeS60Rr8S-s": ["Milestone 3 - Cow Clicker 2 Direct 4.22.2020", "This project was my CS 1520 group's final presentation for our game Cow Clicker 2. You can still play the game!"],
		"SJF4gl2k9Hs": ["The End is Nigh!", "This project was for the Minicast..."],
		"_ZRU6ovWhHM": ["The Return", "This project was for the Essay Film..."],
	}
	return flask.render_template('exhibits.html', page_title='THE MUSEMU', videos=video_map)


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
