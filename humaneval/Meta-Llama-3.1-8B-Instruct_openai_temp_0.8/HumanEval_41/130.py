### Car Collision Function

```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of car collisions in a simultaneous car race.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The total number of car collisions.
    """
    # Calculate the number of collisions using the formula: (n * (n - 1)) / 2
    # This is because each car in the left-to-right set can collide with (n - 1) cars
    # in the right-to-left set, and there are n cars in the left-to-right set.
    collisions = (n * (n - 1))

    # Since each collision is counted twice (once for each car involved), we need to
    # divide the result by 2 to get the correct number of collisions.
    collisions //= 2

    return collisions

# Example usage:
n = 3  # Number of cars in each direction
print(f"The number of collisions with {n} cars in each direction is: {car_race_collision(n)}")
```

This script uses the mathematical formula to calculate the number of collisions between cars moving in opposite directions. The formula `(n * (n - 1)) / 2` calculates the number of unique pairs of cars that can collide, and then this result is divided by 2 to get the actual number of collisions. The result is then returned by the function.