```python
def car_race_collision(n: int) -> int:
    """
    Calculates the number of car collisions in a straight line car racing scenario.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions between cars moving in opposite directions.
    """
    # The total number of pairs of cars is n * n. However, each pair has been counted twice (once for each car in the pair),
    # so we divide by 2 to avoid double counting.
    # The formula 2*n*(n-1) is derived from the formula for combinations (n choose 2) or from a simple mathematical derivation.

    return 2 * n * (n - 1)

# Example usage:
print(car_race_collision(5))
```

This script defines the `car_race_collision` function and uses it to calculate the number of collisions in a scenario where `n` cars are moving in each direction. The function uses the mathematical formula `2*n*(n-1)` to derive the number of collisions. The result is then printed to the console.