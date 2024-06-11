import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0.2, 0.5, 0.33, 0.5, 0.6,0.1,0.75,0.96]
y = [23,23,24,25,25,26,27,28]

plt.plot(x, y)
plt.xlabel("magnitude")
plt.ylabel("Quotient")
plt.title("experiment")
plt.show()