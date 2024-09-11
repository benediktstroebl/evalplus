```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between cars moving left to right and cars moving right to left.

    Parameters:
    n (int): The number of cars in each set.

    Returns:
    int: The number of collisions.
    """
    return n * (n - 1) // 2 * 2


# Example usage:
print(car_race_collision(5))  # Output: 20
print(car_race_collision(10))  # Output: 90
```

This script uses the formula for combinations (n * (n - 1) // 2) to calculate the number of ways two sets of n cars can collide, then multiplies this by 2 to account for the two directions of movement. The result is the total number of collisions.