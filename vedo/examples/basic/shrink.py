"""Shrink mesh polygons
to make the inside visible"""
from vedo import *

pot = load(datadir+"teapot.vtk").shrink(0.75)

s = Sphere(r=0.2).pos(0, 0, -0.5)

show(pot, s, __doc__, axes=1, viewup="z")
