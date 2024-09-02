

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
    cars_left = set(range(n))
    cars_right = set(range(n))
    count = 0

    while len(cars_left) > 0 and len(cars_right) > 0:
        left = cars_left.pop()
        right = cars_right.pop()
        if left < right:
            cars_left.add(left+n)
        else:
            cars_right.add(right+n)
            count += 1

    return count
