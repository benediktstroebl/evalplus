

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
    if n < 1:
        raise ValueError("n must be positive.")
    if n > 200:
        return 0
    count = 0
    for i in range(1, n):
        for j in range(i, n):
            if i * j > n:
                continue
            count += car_race_collision_helper(n, i, j)
    return count

assert car_race_collision(8) == 0
assert car_race_collision(10) == 1
assert car_race_collision(12) == 2
assert car_race_collision(14) == 4
assert car_race_collision(126) == 24
assert car_race_collision(128) == 64
assert car_race_collision(134) == 132
assert car_race_collision(140) == 272
assert car_race_collision(142) == 636
assert car_race_collision(144) == 1440
assert car_race_collision(146) == 4860
assert car_race_collision(148) == 7680
assert car_race_collision(150) == 1296000
assert car_race_collision(152) == 2520000
assert car_race_collision(154) == 57600000
assert car_race_collision(156) == 100000000
assert car_race_collision(158) == 17600000000
assert car_race_collision(160) == 32000000000
assert car_race_collision(162) == 640000000000
assert car_race_collision(164) == 1200000000000
assert car_race_collision(166) == 1560000000000
assert car_race_collision(168) == 2520000000000
assert car_race_collision(170) == 576000000000
assert car_race_collision(172) == 1000000000000
assert car_race_collision(174) == 1760000000000
assert car_race_collision(176) == 32000000000
assert car_race_collision(178) == 6400000000000
assert car_race_collision(180) == 12000000000000
assert car_race_collision(182) == 15600000000000
assert car_race_coll