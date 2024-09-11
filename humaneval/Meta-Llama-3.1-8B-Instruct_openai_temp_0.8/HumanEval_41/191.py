```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race with n cars moving left to right and n cars moving right to left.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    # Each pair of cars that are in the same position will result in a collision.
    # The total number of positions is equal to the number of left-moving cars.
    # For each pair of cars in the same position, there is a left-moving car and a right-moving car that collide.
    # So, we can calculate the total number of collisions using the formula for combinations.
    return n * (n - 1) // 2


# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This script uses the formula for combinations to calculate the number of collisions. The formula is `n * (n - 1) / 2`, where `n` is the number of items. In this case, each pair of cars in the same position results in a collision, so the formula gives the total number of collisions.