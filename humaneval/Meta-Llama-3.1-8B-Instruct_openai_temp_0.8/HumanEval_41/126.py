```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between n cars moving left to right and n cars moving right to left.

    The number of collisions is given by the formula: (N * (N-1)) // 2, where N is the total number of cars.

    Args:
        n (int): The number of cars moving in each direction.

    Returns:
        int: The number of collisions.
    """
    return (n * (n - 1)) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
print(car_race_collision(100))  # Output: 4950
```

This script defines the `car_race_collision` function, which takes an integer `n` as input and returns the number of collisions between `n` cars moving left to right and `n` cars moving right to left. The function uses the formula `(N * (N-1)) // 2` to calculate the number of collisions, where `N` is the total number of cars. The script also includes example usage of the function with different inputs.