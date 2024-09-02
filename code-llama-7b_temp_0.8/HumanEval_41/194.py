

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    #Initialize car number and counter
    cars_left_to_right = n
    cars_right_to_left = n
    collision_count = 0

    #Loop until cars_left_to_right and cars_right_to_left are both 0
    while (cars_left_to_right != 0 and cars_right_to_left != 0):
        cars_left_to_right -= 1
        cars_right_to_left -= 1
        if cars_left_to_right == 0:
            cars_right_to_left -= 1
        elif cars_right_to_left == 0:
            cars_left_to_right -= 1
        else:
            collision_count += 1

    return collision_count
