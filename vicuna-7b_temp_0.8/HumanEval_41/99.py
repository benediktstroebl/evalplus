

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
    # Declare variables
    l_cars, r_cars = divider(n)  # The left cars and the right cars
    total = 0  # The total number of collisions

    # Iterate through cars in each set
    for i in range(0, len(l_cars), 2):
        # Declare variables
        left_car, right_car = l_cars[i], l_cars[i+1]
        _, _, r_car = r_cars[i], r_cars[i+1], r_cars[i+2]
        # Check for collision
        if right_car.x < left_car.x and r_car.x < r_car.x:
            total += 1

    return total