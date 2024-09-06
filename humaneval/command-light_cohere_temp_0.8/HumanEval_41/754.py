```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. 

    All cars are in the same speed; two cars
    will collide when a car that's moving left to right hits a car that's
    moving right to left.
    The function outputs number of the collisions.

tests:
def test_car_race_collision():
    """
    Test cases for the car_race_collision function
    """
    return car_race_collision(10) == 5
```