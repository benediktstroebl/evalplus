

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

    # Calculate the time each car needs to travel
    time = n * 60 #convert seconds to minutes

    # Initialize variables to keep track of the number of cars that have passed
    pass_left = 0
    pass_right = 0

    # Iterate over all cars
    for i in range(n):
        # If the car is moving left to right
        if i % 2 == 0:
            # Update the number of cars that have passed
            pass_left += 1

        # If the car is moving right to left
        elif i % 2 == 1:
            # Update the number of cars that have passed
            pass_right += 1

    # Return the number of collisions
    return pass_left + pass_right - 2