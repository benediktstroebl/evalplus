

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
    cars = n * 2
    collisions = 0
    left = 0
    right = cars - 1

    while left < right:
        if left % 2 == 0:
            left += 1
            if right < cars:
                right += 1
            else:
                right -= 1
        else:
            left += 1
            if right < cars:
                right -= 1
            else:
                right += 1
        collisions += 1
    return collisions


