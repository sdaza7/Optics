import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#Importar Imagen
img = mpimg.imread('IM1.jpeg')
#Mostrar la Imagen
plt.imshow(img,cmap='gray')
#Seleccionar Puntos
u = plt.ginput(2)
#Guardar Valores
u1, u2 = u[0]
v1, v2 = u[1]
#Valor del Pixel
pixelu=img[int(u2), int(u1)]
pixelv=img[int(v2), int(v1)]
print(pixelu, pixelv)
#Recorte
plt.clf()
IR = img[int(u2):int(v2),int(u1):int(v1)]
plt.imshow(IR,cmap='gray')
plt.show()
