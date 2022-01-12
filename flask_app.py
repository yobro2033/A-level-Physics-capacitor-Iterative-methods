from columnar import columnar
import numpy as np
from matplotlib import pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dash():
    return render_template('iterative.html')

@app.route('/search')
def home():
    capacitor = request.form['capacitor']
    voltage = request.form['voltage']
    resistance = request.form['resistance']
    timeInterval = request.form['timeInterval']
    numberLoop = request.form['numberLoop']
    
    initialCharge = capacitor*voltage
    t = 0
    finalCharge = initialCharge
    attempt = 0

    data = []
    while attempt < numberLoop+1:
        #Variable
        tprint = t
        current = finalCharge / (capacitor*resistance)
        #Variable
        currentprint = round(current,6)
        t = t + timeInterval
        #Variable
        initialChargeprint = round(initialCharge,6)
        charge = current*timeInterval
        #Variable
        chargeprint = round(charge,6)
        data.append([tprint,initialChargeprint,currentprint,chargeprint])
        finalCharge = initialCharge - charge
        initialCharge = finalCharge
        attempt = attempt + 1

    headers = ['t','Q','I','ΔQ']
    table = columnar(data, headers, no_borders=True)
    print(table)

    graphData = []
    for dat in data:
        chargeGraph = dat[1]
        timeGraph = dat[0]
        graphData.append([chargeGraph,timeGraph])

    mpltData = np.array(graphData)
    x,y = mpltData.T
    plt.scatter(x,y)
    plt.show()
