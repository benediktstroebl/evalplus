Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move in the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    collisions = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i != j and (i + j) % 2 == 0:
                collisions += 1
            j += 1
        i += 1
    return collisions
```

This function uses two nested loops to iterate through all possible collisions between the two sets of cars. The result is then returned as the value of the collisions variable.