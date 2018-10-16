from PIL import Image
import os
var = "ok"
image1 = Image.open("Gobelin.png")

"""image1.show()""" #afficher l'image

"""image1.save("Gobelin.png")""" #Sauvegarder dans un nouveau format

"""for images in os.listdir('.'):
	if images.endswith('.jpg'):
		i = Image.open(images)""" #Parcourir les images au format jpeg

def size(size = (250,250)):
	image1.thumbnail(size)
	name = ("Gobelin_{0}px.jpg").format(size[0])
	image1.save(name)

size(size=(300,300))