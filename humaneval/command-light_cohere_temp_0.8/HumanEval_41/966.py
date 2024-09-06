```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed and move perfectly along the line.

    The two cars that move towards each other simultaneously
    and move into the same space due to the law of conservation of space. This results in the collision. The cars can continue moving in their same direction, but they are infinitely strong, so they continue moving in their original trajectories.

    The function returns the number of collisions.

test_collision_count(100):
    assert car_race_collision(100) == 5
```