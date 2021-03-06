"""Draw the isolines and isobands
of a scalar field on a surface"""
from vedo import *

mesh = ParametricShape('RandomHills').printInfo()
# RandomHills already has an active scalar associated 
# to points so assign it a colormap:
mesh.cmap('terrain')

isol = mesh.isolines(n=10).color('w')

isob = mesh.clone().isobands(n=5).addScalarBar()

show([(mesh, isol, __doc__), isob], N=2, axes=1)
