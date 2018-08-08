from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	fav_players = ["Leonil Messi","Waseem Lawen","Laith Husseini"]
	return render_template("index.html", players=fav_players, likes_same_sport=True)
	

if __name__ == '__main__':
   app.run(debug = True)