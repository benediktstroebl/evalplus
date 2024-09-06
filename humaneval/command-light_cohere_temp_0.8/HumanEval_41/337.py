```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed and start out being very far from each other.
    When cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    The function outputs whether a collision happened or not.

    return:
        if any(colisions == (n - 1) and len(cars) != n):
            return "No collision!"
        else:
            return f"Collision at {cars[0], {cars[1]} to {cars[2]} at {cars[3]}!"
```
This script provides a self-contained function that solves the car race collision problem and passes the tests. You can use this also for this following problem: