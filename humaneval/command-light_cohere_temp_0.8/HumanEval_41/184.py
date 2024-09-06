```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and are infinitely sturdy and strong.
    When a car that's moving left to right hits a car that's moving right to left, the collision is calculated using the formula: n * (n - 1) = 0.
    The cars continue moving in their original direction, as if they did not collide.
    The function returns the number of collisions that meet the collision criteria.
    """
return n * (n - 1)
```
The function returns the number of collisions that meet the criteria.