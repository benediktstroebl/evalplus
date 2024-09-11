```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The number of collisions.
    """
    # The formula to calculate the number of collisions is n choose 2, which is (n * (n - 1)) // 2
    # This is because for each pair of cars in the left-to-right direction, there is a corresponding car in the right-to-left direction that can collide with it.
    return (n * (n - 1)) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
```

This script uses the formula `n * (n - 1) // 2` to calculate the number of collisions. This formula is derived from the fact that for each pair of cars in the left-to-right direction, there is a corresponding car in the right-to-left direction that can collide with it. The `//` operator is used for integer division to ensure that the result is an integer.