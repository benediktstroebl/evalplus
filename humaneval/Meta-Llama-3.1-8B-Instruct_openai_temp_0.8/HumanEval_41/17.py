```python
def car_race_collision(n: int):
    """
    Calculates the number of collisions in a car race scenario.

    Args:
    n (int): The number of cars driving left to right and right to left.

    Returns:
    int: The number of collisions.
    """
    return n * (n - 1) // 2


# Example usage:
n = 5
print(f"Number of collisions when n = {n}: {car_race_collision(n)}")
```

This script uses the combination formula, which is `n * (n - 1) / 2`, to calculate the number of pairs of cars (or collisions) on the road. The reasoning behind this is as follows:

- There are `n` cars moving left to right. We can choose any two of these cars to collide in `C(n, 2) = n * (n - 1) / 2` ways.
- The same logic applies to the cars moving right to left.
- Therefore, the total number of collisions is `n * (n - 1) / 2` for each set of cars, and since there are two sets of cars, the total number of collisions is `2 * n * (n - 1) / 2`, which simplifies to `n * (n - 1)`.
- However, the problem description mentions that pairs of cars are counted twice (once in each direction), so we divide the total by 2 to avoid double-counting.