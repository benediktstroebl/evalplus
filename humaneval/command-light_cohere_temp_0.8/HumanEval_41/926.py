```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars will intended to collide when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    return:
    This function outputs the number of collisions that occur.

test_car_race_collision(1):
    assert car_race_collision(1) == 0

test_car_race_collision(5):
    assert car_race_collision(5) == 2

test_car_race_collision(10):
    assert car_race_collision(10) == 4

test_car_race_collision(100):
    assert car_race_collision(100) == 26

```
This Python script defines a function called `car_race_collision`, which simulates a head-to-head collision between two vehicles on a straight road. The function takes an integer argument `n` that represents the number of vehicles initially positioned on the road. The function then outputs the number of collisions that occur. The `test_car_race_collision` function provides a few test cases to ensure that the `car_race_collision` function behaves correctly.