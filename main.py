import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def root():
	return flask.render_template('index.html', page_title='About the Museum')

@app.route('/exhibits')
@app.route('/exhibits.html')
def museum():
	video_map = {
		"-O2pFd_ClTY": ["Narnia State Constitution Project", "This was my first big video project. It was made for the State Constitution Project in my 9th grade civics class. Each group needed to create a State Constitution for their fictional state; ours allowed one hour of total anarchy every week."],
		"h9l4QsT2zxs": ["Stuttgart Attractions", "This was my first time using a greenscreen. This project was made for my 10th grade German class to suggest vacation destinations to the teacher's friend. She used all of our projects as an aid when planning her vacation."],
		"jywTa7M09Iw": ["The Complete Idiot's Guide to Russia Under Peter the Great", "This project was made for an 11th grade Russian History seminar. Its focus is on Peter the Great."],
		"FYMsJqgKRVI": ["Cooking with Carter (S1E2): Bartleby's Omelette", "This project was made for a 12th grade short story English assignment. Technically, this is actually the first episode of Cooking with Carter, the whole \"second episode\" thing is just branding."],
		"dic16VrTIEI": ["Group Storytelling: Phillip II and Elizabeth I", "This project was made for a 12th grade Western Civ II assignment. We had multiple group projects I made videos for; this one involved multiple different kinds of footage."],
		"bDYI3WQvziI": ["NYG Beforehand Promo", "This project wasn't made for school, but it's definitely noteworthy. Over the course of 2 months, I directed and coordinated shots in order to piece together this promo and present it to the congregation."],
		"k7_LgEGGTwo": ["Interview Podcast", "This project was made for the interview podcast project in ENGCMP 610 during sophomore year. I didn't want to grab someone else to interview, so I talked to myself in the Whisper Room."],
		"nVr6fX_cwaA": ["Star Wars: Episode XV - Thanksgiving Break", "This project is my magnum opus. It was made as my final project for ENGCMP 610 in sophomore year. If I had more time, it would've been longer, but it's already amazing as is."],
		"SeS60Rr8S-s": ["Milestone 3 - Cow Clicker 2 Direct", "This project was my CS 1520 group's final presentation for our game Cow Clicker 2. Milestone 1 didn't have a video because that presentation was given before COVID hit. You can still <a href=\"https://cow-clicker-2.appspot.com/\" target=\"_Blank\">play the game</a>!"],
		"SJF4gl2k9Hs": ["The End is Nigh!", "This podcast was created for the Minicast project in ENGCMP 1130. I chose to follow the theme of prophecy for the course, spurred on by the dreams of Pastor Dana (discussed in this video)."],
		"_ZRU6ovWhHM": ["The Return", "This project was created for the Essay Film project in ENGCMP 1130. This took a lot of editing, and I achieved the effect I'd hoped to pretty well via lots of layered translucent footage."],
	}
	return flask.render_template('exhibits.html', page_title='The Project Museum', videos=video_map)


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
