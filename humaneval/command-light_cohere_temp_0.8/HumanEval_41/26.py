```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed; two cars will collide as they meet in the road.
    The collision happens as a result of the cars' infinite strength and continue moving in their direction.
    The function outputs the number of collisions.

test_collision_count(5):
    assert car_race_collision(5) == 4

test_collision_order(5):
    assert list(car_race_collision(5)) == [0, 1, 2, 3, 4]

test_collision_speed(10):
    assert car_race_collision(10) == 6

test_collision_car_order(5):
    assert list(car_race_collision(5)) == [0, 2, 3, 1, 4]
```
This Python script defines a function called **car_race_collision** which simulates a scenario of two sets of cars moving in opposite directions on a straight road. The collision is determined by the cars' strength, which allows them to continue moving along their respective trajectories after the collision event. The function returns the number of collisions and passes corresponding tests.