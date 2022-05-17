import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.placement

def open_and_setup_model_view(fp):
    model = ifcopenshell.open(fp)
    return model


def euc_dist3(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

def walls_test(model):
    walls = model.by_type("IfcWall")
    if len(walls) > 5:
        return 'There are more than 5 walls [OK]'
    else:
        return 'There are less than 5 walls [FAIL]'

def distance_to_staircase_test(model):
    doors = model.by_type("IfcDoor")
    stairs = model.by_type("IfcStair")

    door_coords = []
    stair_coords = []
    for door in doors:
        location = ifcopenshell.util.placement.get_local_placement(door.ObjectPlacement)
        pos = location[0:3, 3]
        door_coords.append(pos)

    for stair in stairs:
        location = ifcopenshell.util.placement.get_local_placement(stair.ObjectPlacement)
        pos = location[0:3, 3]
        stair_coords.append(pos)

    for door in door_coords:
        for stair in stair_coords:
            if euc_dist3(door, stair) > 2000:
                return 'The door {} is too far from the staircase [FAIL]'.format(door.Name)
            else:
                return 'All doors are close within 2m of a staircase [OK]'


if __name__ == '__main__':
    s = ifcopenshell.geom.settings()
    s.set(s.USE_WORLD_COORDS, True)
    model = open_and_setup_model_view("220307.MusterIFC_prm4.ifc")
    result_walls_test = walls_test(model)
    print('The walls test yielded the following result : {}'.format(result_walls_test))

    result_distance_to_stairs = distance_to_staircase_test(model)
    print('The distance to stairs test yielded the following result : {}'.format(result_distance_to_stairs))

    