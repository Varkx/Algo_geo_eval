# coding: utf-8
import halfedge_mesh
from random import *
import math

# .off are supported
mesh = halfedge_mesh.HalfedgeMesh("tests/data/cube_highres.off")

"""
Calcul l'angle diadrale de chaque facet, pour chaque face on parcour ses demi arrête et on ajoute
sa valeur dans le tableau que l'on retourne
"""
def calcul_angle_dia():
    valeurs = []
        
    for f in mesh.facets:
        first = f.halfedge.get_angle_normal()
        second = f.halfedge.next.get_angle_normal()
        third = f.halfedge.next.next.get_angle_normal()
        res = (first + second + third)/3
        valeurs.insert(f.index,res)
    return valeurs



"""
Calcul le minimum et le maximum dans la tab valeur
"""
def min_max_graph(valeurs):

    res = [] 
    
    for i in valeurs:
        j = (i-min(valeurs))/(max(valeurs)-min(valeurs))
        res.append(j)
    
    return res

"""
Convertie nos valeurs en degrèes
"""
def degree_convert(valeurs):
    for v in valeurs :
        print((v/math.pi)*180)
       
"""
Colorie chaque face d'une couleur du rouge vers le blanc en fonction de sa grandeur
"""
def color_values(valeurs):
    max_angle = max(valeurs)
    min_angle = min(valeurs)

    colors = []

    for v in valeurs:
        v = (v  * 255 / 1.0)
        g = round((math.sin(0.024 * v + 0) * 127 + 128) / 255, 3)
        b = round((math.sin(0.024 * v + 2) * 127 + 128) / 255, 3)

        colors.append((1.0, g, b, 1.0))
    return colors 

def ceil_fix(seuil,valeurs):
    res = [] 

    for v in valeurs:
        if v > seuil :
            res.append(0)
        else:
            res.append(1)

    return res


def avg_values(valeurs):
    tmp = 0
    count = 0

    for v in valeurs:
        tmp += v
        count += 1

    return tmp/count

def ceil_by_avg(valeurs):

    seuil = avg_values(valeurs)
    res = [] 

    for v in valeurs:
        if v > seuil :
            res.append(0)
        else:
            res.append(1)

    return res

#Calcul des angles diedraux

valeurs = mesh.calcul_angle_dia()
print(valeurs)

#Coloration
distances = mesh.get_distances(0)
print(distances)

id = randint(0,len(mesh.vertices)-1)
distances = mesh.get_distances(id)
mesh.save_off("cubeteststst.off",values = distances)

#Segmentation
seuil = 0.5 
# ceil_fix(seuil,valeurs)


