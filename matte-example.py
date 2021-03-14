import matplotlib.pyplot as plt
import numpy as np

plt.style.use('Matte')

t = np.arange(0, 2, 0.02)
s1 = 1.5 + np.sin(2 * np.pi * t)
s2 = 2.0 + np.sin(2 * np.pi * t)
s3 = 2.5 + np.sin(2 * np.pi * t)
s4 = 3.0 + np.sin(2 * np.pi * t)
s5 = 3.5 + np.sin(2 * np.pi * t)

plt.figure(figsize=(14,6))

plt.plot(t,s1)
plt.plot(t,s2)
plt.plot(t,s3)
plt.plot(t,s4)
plt.plot(t,s5)

plt.title('Matte Theme Example')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')

legend = ['Curve 1', 'Curve 2', 'Curve 3', 'Curve 4', 'Curve 5']
plt.legend(legend)
plt.savefig('./matte-theme-example.png')