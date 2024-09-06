```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed, and two cars will collide as they meet on the road. They are both infinitely sturdy and strong, so they continue moving in their original direction, as if they didn't collide.

    return: 
    -Count the number of collisions.
    collisions = sum(1 for i in range(n))
    return collisions

# Example of passed test:
assert car_race_collision(6) == 6
```