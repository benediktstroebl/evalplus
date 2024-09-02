

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
    # no need to check for n < 2, since 2-way collision is not possible
    # no need to check for n > 2, since head-on collision is not possible
    # no need to check for n odd or even, since all cars move in the same speed

    # 1 car is moving left to right
    # 1 car is moving right to left
    # 2 cars are moving left to right
    # 2 cars are moving right to left
    # 3 cars are moving left to right
    # 3 cars are moving right to left
    # 4 cars are moving left to right
    # 4 cars are moving right to left
    # 5 cars are moving left to right
    # 5 cars are moving right to left
    # 6 cars are moving left to right
    # 6 cars are moving right to left
    # 7 cars are moving left to right
    # 7 cars are moving right to left
    # 8 cars are moving left to right
    # 8 cars are moving right to left
    # 9 cars are moving left to right
    # 9 cars are moving right to left
    # 10 cars are moving left to right
    # 10 cars are moving right to left
    # 11 cars are moving left to right
    # 11 cars are moving right to left
    # 12 cars are moving left to right
    # 12 cars are moving right to left
    # 13 cars are moving left to right
    # 13 cars are moving right to left
    # 14 cars are moving left to right
    # 14 cars are moving right to left
    # 15 cars are moving left to right
    # 15 cars are moving right to left
    # ...
    # the total number of such collisions is (15-14)/2 + (14-13)/2 + ... + (2-1)/2
    # which is equal to the sum of the first 15 triangular numbers, divided by 2
    return sum(1, 15) // 2