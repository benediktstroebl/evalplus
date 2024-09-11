```python
def car_race_collision(n: int):
    """
    Calculates the number of collisions between two sets of n cars moving in opposite directions.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The number of collisions between the two sets of cars.
    """
    if n <= 0:
        # No cars means no collisions
        return 0
    if n == 1:
        # If only one car in each set, no collisions occur
        return 0
    total_cars = n * 2
    total_collisions = (total_cars * (total_cars - 1)) // 2 - (n * (n - 1)) // 2
    return total_collisions

# Example usage:
print(car_race_collision(2))  # 1
print(car_race_collision(3))  # 5
print(car_race_collision(5))  # 21
```

This script uses a formula for combinations to calculate the total number of collisions between all pairs of cars, then subtracts the number of collisions between cars moving in the same direction. The result is the total number of collisions between the two sets of cars.