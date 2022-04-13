# coding: utf-8
import halfedge_mesh
from random import *



# .off are supported
mesh = halfedge_mesh.HalfedgeMesh("tests/data/cube_highres.off")

# Returns a list of Vertex type (in order of file)--similarly for halfedges,
# and facets
mesh.vertices

#The number of facets in the mesh
len(mesh.facets)

# Get the 10th halfedge
mesh.halfedges[10]

#Get distance of the halfedge
distances = mesh.get_distances(0)
print(distances)

id = randint(0,len(mesh.vertices)-1)
distances = mesh.get_distances(id)
idmax = max(enumerate(distances),key = lambda x: x[1])[0]   

distances2 = mesh.get_distances(idmax)
idmax2 = max(enumerate(distances2),key = lambda x: x[1])[0]

#Get the halfedge that starts at vertex 25 and ends at vertex 50
#will not work with a random mesh
#mesh.get_halfedge(25, 50)

# Iterate over the vertices of the mesh
for i in mesh.vertices:
    print(i.get_vertex())
#save the file
mesh.save_off("cubeteststst.off",values = distances)

cc = mesh.visit()
print(cc)
print(mesh.calculX(cc))
valeurs = mesh.calcul_angle_dia()
print(valeurs)




