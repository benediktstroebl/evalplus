

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
    # Create the array with the cars
    cars = [i for i in range(n)]
    # Variable that will count the collisions
    count = 0
    # Create the variable for the offset
    offset = n // 2
    # While there is cars
    while cars:
        # Move all cars one place to the left
        for i in range(len(cars)):
            cars[i] -= 1
        # If the car is on an index that is the same as the offset,
        # there is a collision, then the car is removed
        for i in range(len(cars)):
            if cars[i] == offset:
                cars.remove(cars[i])
                count += 1
    return count


