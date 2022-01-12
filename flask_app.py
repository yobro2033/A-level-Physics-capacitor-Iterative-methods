from columnar import columnar
import numpy as np
from matplotlib import pyplot as plt

print("\nWelcome to Iterative Capacitor table calculation!\nPlease follow the instruction to retrieve the table data.\n\n")
capacitor = float(input("Please enter capacitance (e.g 1500 or 0.00025): "))
voltage = float(input("Please enter voltage (e.g 1500 or 0.00025): "))
resistance = float(input("Please enter resistance (e.g 1500 or 0.00025): "))
timeInterval  = float(input("Please enter time interval (e.g 1 or 0.25): "))
numberLoop = int(input("How many time(s) you want to iterate? (e.g 5 or 20) "))
initialCharge = capacitor*voltage
t = 0
finalCharge = initialCharge
attempt = 0

print("\n------------Iterative Table------------")
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
