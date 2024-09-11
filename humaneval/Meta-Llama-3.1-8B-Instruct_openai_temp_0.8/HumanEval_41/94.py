```python
def car_race_collision(n: int) -> int:
    """
    Calculates the number of collisions in a car race scenario.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    # Calculate the total number of pairs of cars
    total_pairs = n * (n - 1) // 2

    # If there's only one car in one direction, or no cars at all, there's no collision
    if n < 2:
        return 0

    # Every pair of cars from opposite directions will collide exactly once
    total_collisions = total_pairs

    return total_collisions

# Test the function
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This script defines a function `car_race_collision` that calculates the number of collisions in a car race scenario with `n` cars driving left to right and `n` cars driving right to left. The function uses the formula for the number of pairs of elements in a set of `n` elements to calculate the total number of pairs of cars, and then multiplies this by 1 (since each pair will collide once) to get the total number of collisions. The function returns this total number of collisions. The script also includes test cases to demonstrate the function's behavior.