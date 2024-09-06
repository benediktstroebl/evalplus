

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
    assert 0 <= n < 100
    return int(factorial(n) / (factorial(n - 2) * 2))


assert car_race_collision(0) == 0
assert car_race_collision(1) == 0
assert car_race_collision(2) == 0
assert car_race_collision(3) == 0
assert car_race_collision(4) == 1
assert car_race_collision(5) == 2
assert car_race_collision(6) == 4
assert car_race_collision(7) == 10
assert car_race_collision(8) == 4
assert car_race_collision(9) == 4
assert car_race_collision(10) == 10
assert car_race_collision(100) == 1290
