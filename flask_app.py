from columnar import columnar
import numpy as np
from matplotlib import pyplot as plt
from flask import Flask, render_template, request
import base64
import io 

app = Flask(__name__)

@app.route('/')
def dash():
    return render_template('iterative.html')

@app.route('/search', methods=['POST', 'GET'])
def home():
    capacitor = request.form['capacitor']
    capacitor = float(capacitor)
    voltage = request.form['voltage']
    voltage = float(voltage)
    resistance = request.form['resistance']
    resistance = float(resistance)
    timeInterval = request.form['timeInterval']
    timeInterval = float(timeInterval)
    numberLoop = request.form['numberLoop']
    numberLoop = int(numberLoop)
    
    initialCharge = capacitor*voltage
    t = 0
    finalCharge = initialCharge
    attempt = 0

    data = []
    data1 = []
    while attempt < numberLoop+1:
        #Variable
        tprint = round(t,2)
        current = finalCharge / (capacitor*resistance)
        #Variable
        currentprint = round(current,6)
        t = t + timeInterval
        #Variable
        initialChargeprint = round(initialCharge,7)
        charge = current*timeInterval
        #Variable
        chargeprint = round(charge,10)
        data1.append({'tprint': tprint, 'initialChargeprint': initialChargeprint, 'currentprint': currentprint, 'chargeprint': chargeprint})
        data.append([tprint,initialChargeprint,currentprint,chargeprint])
        finalCharge = initialCharge - charge
        initialCharge = finalCharge
        attempt = attempt + 1

    graphData = []
    for dat in data:
        chargeGraph = dat[1]
        timeGraph = dat[0]
        graphData.append([chargeGraph,timeGraph])

    mpltData = np.array(graphData)
    img = io.BytesIO()
    x,y = mpltData.T
    plt.scatter(x,y)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    
    return render_template("result.html", data1=data1, imagen={ 'imagen': plot_url })
