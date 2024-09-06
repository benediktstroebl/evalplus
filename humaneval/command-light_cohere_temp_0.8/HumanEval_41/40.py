```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    Two cars are move in the same speed and direction to collide.
    :return max(0, n - sum([max(c) - min(c) for c in collisions]))
    # Your code here
    collisions = [c for c in range(n)]
    # Build a list of the minimum and maximum speeds for each car
    # Add this to the collisions list
    return max(0, n - sum([max(c) - min(c) for c in collisions]))
```