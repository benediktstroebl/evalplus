```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. All cars move in the same speed.
    Two cars intended to collide on collision.
    The function outputs the number of collisions.
n_cars = n  # number of cars
collisions = 0 # number of collisions
for i in range(n_cars):
    if i < n_cars // 2:
        if i + n_cars // 2 >= n_cars:
            collisions += 1
    else:
        collisions += 1
    return collisions
```