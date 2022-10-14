import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#Importar Imagen
img = mpimg.imread('IM1.jpeg')
#Mostrar la Imagen
plt.imshow(img,cmap='gray')
#Seleccionar un punto
u = plt.ginput(1)
print(np.shape(u))
#pixel=img[u]
print(u[0])
u1, u2 = u[0]
print(u2)
IR = img[50:100,100:200]
plt.imshow(IR,cmap='gray')
