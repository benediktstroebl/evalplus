

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

    assert n >= 2, f'At least two cars need to move.  n was {n}'
    assert n % 2 == 0, f'At least one car needs to move left to right, and the other needs to move right to left.  n was {n}'
    
    n_left = n // 2
    n_right = n - n_left

    total_collisions = 0
    for i in range(n_left):
        car_left = i + 1
        car_right = n - car_left
        total_collisions += car_left + car_right

    return total_collisions
