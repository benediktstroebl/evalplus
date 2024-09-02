

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
    # This line is the original O(n^2) solution
    pass

    # This line is the optimized O(nlogn) solution
    left_car = 0
    right_car = n - 1
    while left_car <= right_car:
        if cars[left_car] <= cars[right_car]:
            return right_car - left_car + 1
        left_car += 1

    return 0