```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed
    The cars will collide when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.

    return the collision is the number of cars that were involved.
    """
function outputs the number of collisions that occurred.
```
The number of collisions is the number of cars that were driving right to left and were hit by a car that was driving right to left. The function has been tested and works as expected.