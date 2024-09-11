```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between left-to-right and right-to-left moving cars.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions between the two sets of cars.
    """
    # Calculate the total number of possible pairs between the two sets of cars
    total_pairs = n * (n - 1) // 2  # This is the number of ways to choose two elements from a set of n elements

    # Since the order of the cars doesn't matter (a collision is the same regardless of whether car A hits car B or car B hits car A),
    # we divide the total number of pairs by 2 to avoid counting each collision twice.
    # However, this would be incorrect if some cars are identical (because we would be counting a collision between two identical cars only once),
    # but the problem statement implies that all cars are distinct.
    return total_pairs // 2


# Test the function
print(car_race_collision(5))
```

This script defines the `car_race_collision` function that takes the number of cars `n` in each direction as input and returns the number of collisions between the two sets of cars. The function uses the formula for combinations to calculate the total number of possible pairs between the two sets of cars, and then divides this number by 2 to avoid counting each collision twice. The script also includes a test case with `n = 5` to demonstrate the function's usage.