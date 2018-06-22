# ex_bezier_surface.py
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set evaluation delta
surf.delta = 0.01

# Set up the surface
surf.degree_u = 2
surf.degree_v = 2

with open('test.txt') as f:
    c_lines = f.read().splitlines()
    control_points = []
    for i in c_lines:
        control_points.append([j for j in i.split()])

#control_points = [[0, 0, 0], [0,1,0], [0, 2, 0], [1, 1, 3],
 #                 [0, 2, 0], [1,1,0], [2, 0, 0], [1,0,0], [0, 0, 0]]

surf.set_ctrlpts(control_points, 3, 3)
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 3)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 3)

# Evaluate surface
surf.evaluate()

# Save surface as a .obj file
exchange.save_obj(surf, "bezier_surf.obj")