import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


def makeGraphofMass() :
    InitialMass = float(e2.get())
    DryMass = 2000
    FuelBurnRate = 119
    Time = np.arange(0,(InitialMass-DryMass)/FuelBurnRate)
    Mass = (InitialMass - (FuelBurnRate*Time))
    plt.plot(Time,Mass)
    plt.xlabel('Time')
    plt.ylabel('Mass')
    plt.ylim(DryMass - DryMass/10,((InitialMass) + (InitialMass/10)))
    plt.xlim(-((InitialMass-DryMass)/FuelBurnRate)/10, ((InitialMass-DryMass)/FuelBurnRate) + ((InitialMass-DryMass)/FuelBurnRate)/10)
    plt.show()
    return
def makeGraphofForce() :
    InitialForce = float(e1.get())
##  ISPFunction = ?
##  AtmosFunction = ?
##  StartingAlt = ?
##  Starting ISP = ?
    return
window = tk.Tk()
tk.Label(window, text="Force").grid(row=0)
tk.Label(window, text="Mass").grid(row=1)

e1 = tk.Entry(window)
e2 = tk.Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

MyButton1 = tk.Button(window, text="Mass", width=10, command=makeGraphofMass)
MyButton1.grid(row=2, column=1)

MyButton2 = tk.Button(window, text="Force", width=10, command=makeGraphofForce)
MyButton2.grid(row=2, column=2)

window.mainloop

