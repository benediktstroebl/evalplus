```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed.
    When cars that are moving left to right will hit the cars that are moving right to left, so there will be a collision. When this happens, the cars are infinitely strong, so they will continue moving in their respective trajectories.
    Return the number of collisions.
 # The number of cars is even, we should get the correct amount of collisions:
    return 2 ** n // 2
```