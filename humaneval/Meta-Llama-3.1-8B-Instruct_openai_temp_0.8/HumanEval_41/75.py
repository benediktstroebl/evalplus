```python
def car_race_collision(n: int):
    """
    Calculates the number of car collisions in a simultaneously moving race.

    Args:
        n (int): The number of cars moving left to right and right to left.

    Returns:
        int: The number of collisions between cars.
    """
    # The number of collisions is always (n * (n - 1)) // 2
    # This is because for each of the n pairs of cars moving in opposite directions,
    # there will be a collision.
    # So we just need to calculate the number of pairs, which is n * (n - 1) / 2,
    # rounded down to the nearest whole number.
    return (n * (n - 1)) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This script uses the mathematical formula for combinations to calculate the number of collisions, which is always (n * (n - 1)) // 2, where n is the number of cars moving left to right and right to left. The `//` operator in Python performs integer division, which returns the largest whole number that is less than or equal to the result of the division.