from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

def calc(radius, height):
    areaTop = (3.14 * radius**2)
    areaSides = radius * height * 3.14**2
    areaTotal = areaTop + areaSides
    sqFeet = areaTotal / 144
    mCost = 25 * sqFeet
    lCost = 15 * sqFeet
    totalCost = mCost + lCost
    print(totalCost)
    return totalCost

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def mike():
    return render_template('about.html')

@app.route('/estimate', methods=['Get'])
def estimate():
    return render_template('estimate.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        radius = int(request.form['radius'])
        height = int(request.form['height'])
        print(radius)
        print(height)
        estimateCost = calc(radius, height)

        print(estimateCost)
    return render_template('estimate.html', estimate=estimateCost)


if __name__ == '__main__':
    app.run(debug=True)
