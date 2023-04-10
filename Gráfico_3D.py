from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#definição da superfície e das arestas
x=np.outer(np.linspace(-2,2,10),np.ones(10))

y=x.copy().T

z=np.cos(x ** 3 + y ** 3)

fig=plt.figure()

#sintaxe para 3d plotagem

ax=plt.axes(projection = '3d')

#sintaxe para plotagem
ax.plot_surface(x,y,z,cmap='viridis',edgecolor='green')
ax.set_title('Surface plot python.hub')
plt.show()