

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
    # In this function, we are dealing with the left-to-right cars.
    for i in range(n // 2):
        # We are trying to find the maximum number of cars that can collide
        # if all the cars move at the same speed.
        left_start = i * 2
        left_end = min(i * 2 + 1, n)
        collision_count = 0
        for j in range(left_start, left_end):
            if j % 2 == 1 and j != i:
                collision_count += 1
        return collision_count