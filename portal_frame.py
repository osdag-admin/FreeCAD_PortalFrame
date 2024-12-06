from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.gp import gp_Vec, gp_Trsf, gp_Ax1, gp_Dir, gp_Pnt
from OCC.Display.SimpleGui import init_display
import math

# Import functions from existing scripts
from draw_i_section import create_i_section
from draw_rectangular_prism import create_rectangular_prism

def create_portal_frame(column_height, column_thickness, rafter_length, rafter_thickness, purlin_length, purlin_width, purlin_height, flange_thickness, web_thickness, rafter_angle):
    """
    Create a CAD model of a simple A-shaped steel portal frame.

    Parameters:
    - column_height: Height of the columns
    - column_thickness: Thickness of the I-section columns
    - rafter_length: Length of the rafters
    - rafter_thickness: Thickness of the I-section rafters
    - purlin_length: Length of the purlins
    - purlin_width: Width of the purlins
    - purlin_height: Height of the purlins
    - flange_thickness: Thickness of the I-section flanges
    - web_thickness: Thickness of the I-section web
    - rafter_angle: Angle of inclination of the rafters (in degrees)

    Returns:
    - portal_frame_solid: The portal frame CAD model as a TopoDS_Solid
    """
    # Create the columns
    column = create_i_section(column_thickness, column_thickness, column_height, flange_thickness, web_thickness)
    trsf = gp_Trsf()
    trsf.SetTranslation(gp_Vec(0, 0, 0))  # Position the columns at the origin
    column_transform1 = BRepBuilderAPI_Transform(column, trsf, True).Shape()

    trsf.SetTranslation(gp_Vec(0, 0, column_height))  # Position the second column at the same height
    column_transform2 = BRepBuilderAPI_Transform(column, trsf, True).Shape()

    # Convert angle from degrees to radians
    angle_rad = math.radians(rafter_angle)

    # Create the inclined rafters
    rafter = create_i_section(rafter_length, rafter_thickness, rafter_thickness, flange_thickness, web_thickness)

    # First rafter
    trsf = gp_Trsf()
    trsf.SetRotation(gp_Ax1(gp_Pnt(0, 0, column_height), gp_Dir(1, 0, 0)), -angle_rad)  # Rotate the rafter
    trsf.SetTranslation(gp_Vec(-rafter_length / 2, 0, column_height))  # Move to the top of the columns
    rafter_transform1 = BRepBuilderAPI_Transform(rafter, trsf, True).Shape()

    # Second rafter
    trsf = gp_Trsf()
    trsf.SetRotation(gp_Ax1(gp_Pnt(0, 0, column_height), gp_Dir(1, 0, 0)), angle_rad)  # Rotate the rafter in the opposite direction
    trsf.SetTranslation(gp_Vec(rafter_length / 2, 0, column_height))  # Move to the top of the columns
    rafter_transform2 = BRepBuilderAPI_Transform(rafter, trsf, True).Shape()

    # Create the purlins
    purlin = create_rectangular_prism(purlin_length, purlin_width, purlin_height)
    purlins = []
    num_purlins = 5  # Example number of purlins

    for i in range(num_purlins):
        trsf = gp_Trsf()
        trsf.SetTranslation(gp_Vec(0, (i * 150.0) - ((num_purlins / 2) * 150.0), column_height / 2))  # Evenly spaced purlins
        purlin_transform = BRepBuilderAPI_Transform(purlin, trsf, True).Shape()
        purlins.append(purlin_transform)

    # Combine all parts into one solid
    portal_frame_solid = BRepAlgoAPI_Fuse(column_transform1, column_transform2).Shape()
    portal_frame_solid = BRepAlgoAPI_Fuse(portal_frame_solid, rafter_transform1).Shape()
    portal_frame_solid = BRepAlgoAPI_Fuse(portal_frame_solid, rafter_transform2).Shape()

    for purlin in purlins:
        portal_frame_solid = BRepAlgoAPI_Fuse(portal_frame_solid, purlin).Shape()

    return portal_frame_solid

if __name__ == "__main__":
    # Define the dimensions
    column_height = 4000.0
    column_thickness = 100.0
    rafter_length = 5000.0
    rafter_thickness = 100.0
    purlin_length = 1000.0
    purlin_width = 40.0
    purlin_height = 20.0
    flange_thickness = 10.0
    web_thickness = 5.0
    rafter_angle = 60.0  # Angle in degrees for the inclination of the rafters

    # Create the portal frame
    portal_frame = create_portal_frame(column_height, column_thickness, rafter_length, rafter_thickness, purlin_length, purlin_width, purlin_height, flange_thickness, web_thickness, rafter_angle)

    # Visualization
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(portal_frame, update=True)
    display.FitAll()
    start_display()
