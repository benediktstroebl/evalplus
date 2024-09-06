```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. All cars have the layout and move in a straight path at a constant speed. 
    Two cars want to collide
    When a car that's moving left to right hits a car that's moving right to left, they both continue moving in their trajectory. 

    function outputs the time when two cars collide and the time it takes for the collision to happen.

test_collision = car_race_collision(3)
assert test_collision == 2

```