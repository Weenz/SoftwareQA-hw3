from flask import Flask, request, render_template
from datetime import datetime
import math

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
            

@app.route('/calculator')
def calculator():
    choice = request.args['choice']

    if choice == 'retire':
        return render_template('RetireCalc.html')
    else:
        return render_template('BMICalc.html')


@app.route('/BMIresults')
def BMI():
    feet = float(request.args['feet'])
    inches = float(request.args['inches'])
    weight = float(request.args['weight'])

    weight = weight * 0.45
    height = feet * 12 + inches
    height = height * 0.025
    height = height * height

    bmi = weight / height
    bmi = math.ceil(bmi * 10)/10

    if (bmi <= 18.5):
        value = "Underweight"

    elif ( (bmi > 18.5) and (bmi <= 24.9) ):
        value = "Normal Weight"
    
    elif( (bmi >= 25) and (bmi <= 29.9) ):
        value = "Overweight"
    
    else:
        value = "Obese"

    return render_template('BMIresults.html', value=value, bmi=bmi)

@app.route('/RetireResults')
def RetireCalc():
    age = int(request.args['age'])
    aSalary = int(request.args['aSalary'])
    percentSaved = int(request.args['percentSaved'])
    userGoal = int(request.args['userGoal'])

    yearsReq = int(userGoal / (aSalary * ((percentSaved/100) * 1.35)))

    goalAge = int(math.ceil(age + yearsReq))

    return render_template('RetireResults.html', years = yearsReq, age = goalAge)

if __name__ == '__main__':
    app.run(debug=True)
