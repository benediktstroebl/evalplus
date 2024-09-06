

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
    # Write your code here
    # ...

    # Here is the solution for the problem
    n_cars_left = n // 2
    n_cars_right = n // 2

    # Check for collisions between cars moving left to right
    for i in range(n_cars_left):
        for j in range(i + 1, n_cars_left):
            if (j - i)**2 + (i + 1 - j)**2 <= 4:
                print(i, j)

    # Check for collisions between cars moving right to left
    for i in range(n_cars_right):
        for j in range(i + 1, n_cars_right):
            if (i - j)**2 + (i + 1 - j)**2 <= 4:
                print(i, j)