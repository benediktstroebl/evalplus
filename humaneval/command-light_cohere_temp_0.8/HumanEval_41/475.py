```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. All cars move in the same speed. 
    When two cars are supposed to collide
    when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    return:
    Two cars are randomly selected to collide.
    collisions = sum(1 for i in range(n)) / 2

    the number of collisions is returned.
```