```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed.

    Two cars are collide when a car that's moving left to right hits a car that's moving right to left.
    They're infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.

    The function outputs the number of collisions that happen.
    return: Number of collisions
    """
    Test case:
    return n**2 - 4
```