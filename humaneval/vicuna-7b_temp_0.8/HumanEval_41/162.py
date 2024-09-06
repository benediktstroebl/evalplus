

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

    # sorting the left and right cars
    cars_left = sorted(range(n), key=lambda i: i % 2)
    cars_right = sorted(range(n, n*2), key=lambda i: i % 2)

    # checking for collisions
    for i in range(0, n-1):
        for j in range(i+1, n-1):
            if (cars_left[i] + cars_left[i+1]) > cars_right[j] and (cars_left[i] + cars_left[i+1]) < cars_right[j+1]:
                return 0
            elif (cars_right[j] + cars_right[j+1]) > cars_left[i] and (cars_right[j] + cars_right[j+1]) < cars_left[i+1]:
                return 0

    return 1
