```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed; two cars will collide when moving left-to-right hits right-to-left.
    A little push is to give each car an equal amount of push, so they will end up colliding at the same time, but still moving their original direction.
    return the The number of collisions
    """

    # Two cases to check
    # First, the leftmost car reaches the rightmost car
    # Second, the rightmost car reaches the leftmost car
    # Case 1: Leftmost car hits rightmost car, 2 collisions
    # Case 2: Rightmost car hits leftmost car, 1 collision
    # Case 3: Leftmost car hits leftmost car, 1 collision
    # Total number of collisions: 2 + 1 + 1 = 4 collisions
    return 4
```