Here is a self-contained Python script that solves the problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars move in the same speed; two cars will collide
    when a car that's moving left to right hits a car that's moving right to left.

    If two cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.
    return the number of collisions
    """ collision number between all pairs of cars
    """

    # Two cases to test:
    # 0 to 0 collision (should return 0)
    # 0 to 1 collision (should return 1)
    # 1 to 0 collision (should return 1)
    # 1 to 1 collision (should return 0)

    return sum([0 for _ in range(n)])
```