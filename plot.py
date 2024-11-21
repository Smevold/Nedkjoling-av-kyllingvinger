import math
import numpy as np
import matplotlib.pyplot as plt

# Funksjon for utregning av Newtons avkjølingslov. math.exp tar det som er i parantesen som eksponenten til Eulers tall
def Newtons_avkjolingslov(t):
    temp = 74*math.exp(-0.044*t)+16
    return temp

# Verdier for Newtons avkjølingslov ved t=0 til t=180 for hver heltallsverdi for t
t = np.arange(0, 180, 1)
temp = []
for i in t:
    temp.append(Newtons_avkjolingslov(i))


# Antall minutter etter t=0 hvor det ble gjort målinger
t_maalinger = np.array([0, 0.5, 1, 1.5, 2, 3, 4, 5, 10, 15, 20, 25, 30, 45, 60, 90, 120, 150, 180])
# Målte verdier for T
temp_maalinger = np.array([90, 84, 83, 81, 79, 75, 71, 68, 56, 49, 43, 38, 36, 29, 25, 21, 18, 17, 17])




# Plotting av målte verdier og Newtons avkjølingslov
plt.plot(t_maalinger, temp_maalinger, 'r', label='Målt temp')
plt.plot(t, temp, 'b', label='Newtons Avkjølingslov')

# Pynting av plottet
plt.title('Newtons avkjølingslov på nedkjøling av kyllingvinger')
plt.ylabel('T[\xb0C]')
plt.xlabel('t[min]')
plt.legend()

plt.show()
