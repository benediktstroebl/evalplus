```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.

    :param n: The number of cars driving left to right and right to left.
    :return: The number of collisions.
    """
    collisions = 0
    for i in range(1, n + 1):
        # The left to right cars are moving at speed i
        # The right to left cars are moving at speed n - i + 1
        # We want to ensure we don't count a collision twice
        for j in range(i + 1, n + 1):
            # If the sum of the two cars' speeds is even, they can collide
            if (i + (n - j + 1)) % 2 == 0:
                collisions += 1

    return collisions

# Example usage:
print(car_race_collision(5))
print(car_race_collision(10))
```

This code works by iterating over all pairs of cars and checking if they can collide. If the sum of their speeds is even, they can collide, so we increment the `collisions` counter. Finally, we return the total number of collisions.

Note: This solution assumes that the cars are numbered from 1 to `n` and that the left to right cars are moving at speed `i` and the right to left cars are moving at speed `n - i + 1`. This is a simplification and may not be the only possible interpretation of the problem.