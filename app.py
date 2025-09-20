from flask import Flask,render_template
import database
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/donating')
def donation():
    return render_template('donation.html')

@app.route('/about')
def About():
    return render_template('About.html')

@app.route('/restaurants')
def restaurants():
    data = database.get_restaurants()
    return render_template('restaurant.html',restaurant=data)

@app.route('/charities')
def charities():
    data = database.get_charities()
    return render_template('charities.html',charities=data)

@app.route('/match')
def matches():
    data = database.get_matches()
    return render_template('matches.html',matches=data)

if __name__ == "__main__":
    app.run(debug=True)


