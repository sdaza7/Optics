import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Importar Imagen
img = mpimg.imread('IM1.jpeg')
#Mostrar la Imagen
plt.imshow(img,cmap='gray')
#Seleccionar un punto
u = plt.ginput(1)
print(u)
