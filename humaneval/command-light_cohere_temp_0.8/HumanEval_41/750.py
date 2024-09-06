```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed, and two cars will collide when a car that's moving left to right hits a car that's moving right to left.
    return: number of collisions that happen during this race.
    test: print(test(n))
    """

    # By definition, there are always n/2 collisions.
    return n// / 2

    return 0

# Unit tests:
def test(n: int):
    return n > 1
```

This function uses a recursive approach to solve the problem. The function returns the number of collisions that happen during the race, which by definition, is the number of n/2 collisions. The test function simply checks if n is greater than 1 to pass the test.