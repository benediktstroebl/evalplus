

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
    cars = [1, 4, 7, 3, 5, 1, 3, 2, 5, 7]
    cars = [1, 4, 7, 3, 5, 1, 3, 2, 5, 7]
    return car_race_collision_helper(cars, 1234567890, n)

assert car_race_collision(10) == 23
assert car_race_collision(20) == 57
assert car_race_collision(50) == 352
assert car_race_collision(100) == 736
assert car_race_collision(200) == 1618
assert car_race_collision(500) == 666
assert car_race_collision(1000) == 233
assert car_race_collision(2000) == 743
assert car_race_collision(5000) == 956
assert car_race_collision(10000) == 3137
assert car_race_collision(20000) == 4651
assert car_race_collision(50000) == 11299
assert car_race_collision(100000) == 29955
assert car_race_collision(200000) == 478
assert car_race_collision(500000) == 116507
assert car_race_collision(1000000) == 2859302
assert car_race_collision(2000000) == 52959142
assert car_race_collision(5000000) == 99630067
assert car_race_collision(10000000) == 28584234
assert car_race_collision(2500000) == 47090846
assert car_race_collision(100000000) == 302523703
assert car_race_collision(25000000) == 539149734
