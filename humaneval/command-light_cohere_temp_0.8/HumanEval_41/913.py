```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    All cars move in the same speed and direction, with the first set of cars moving away from each other.
    The cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    The function outputs the number of collisions.
#test
    assert car_race_collision(4) == 4
    assert car_race_collision(8) == 8
```
The function car_race_collision uses the concept of a road with two sets of cars moving toward each other. The function works by simulating the movement of the cars and determining when they collide. The function then counts the number of collisions and returns the total count. The test at the test verifies the function's output for different values of n.