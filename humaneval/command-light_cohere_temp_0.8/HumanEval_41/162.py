```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    All cars move in the same speed. Two cars that are moving to collide
    are considered to have collided. The cars are infinitely sturdy and strong.

    If function outputs True collisions or
    The last state is that both cars continue moving.
    """ return [list(map(lambda x: x, range(2, n))))
```