import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01, 2, 0.01)
y = np.log10(x)/np.arctan(x)

plt.plot(x, y)
plt.show()