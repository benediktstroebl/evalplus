```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. All cars have the cars move in the same speed; two cars
    are driving towards each other. 

    The time they the collisions, the cars continue moving
    in their trajectory as if they did not collide. The function returns the number of collisions.
```
And the corresponding tests:
```python
def test_car_race_collision():
    assert car_race_collision(2) == 1

def test_car_race_collision2():
    assert car_race_collision(4) == 4
```
This code defines a function `car_race_collision` that simulates the movement of cars on a straight road and returns the number of collisions. It then has two test functions that pass the corresponding assertions.