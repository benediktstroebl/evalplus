

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

    # Divide the cars into 2 groups
    n = n // 2
    cars_l2r = range(1, n+1)
    cars_r2l = range(n+1, 2*n+1)

    # Initialize the array to store the number of cars collided between
    # the two group of cars
    number_of_collisions = [0] * n

    # Find the number of cars that collided between two groups of cars
    for i in range(0, n):
        for j in range(0, n):
            if abs(cars_l2r[i] - cars_r2l[j]) <= 1:
                number_of_collisions[i] += 1
                number_of_collisions[j] += 1

    # Return the total number of collisions
    return sum(number_of_collisions)

