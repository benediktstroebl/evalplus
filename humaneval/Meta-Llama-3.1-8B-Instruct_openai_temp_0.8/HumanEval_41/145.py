```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race.

    This function uses the concept of combinations to calculate the number of collisions.
    For n cars traveling left to right and n cars traveling right to left, the total number
    of collisions is the number of ways to choose 2 cars from the total of 2n cars.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions.
    """
    # Calculate the total number of cars (left to right + right to left)
    total_cars = 2 * n
    
    # The number of collisions is the number of ways to choose 2 cars from the total
    collisions = total_cars * (total_cars - 1) // 2
    
    return collisions

# Example usage:
n = 5
print(f"Number of collisions for {n} cars in each direction:", car_race_collision(n))
```

This script uses the concept of combinations to calculate the number of collisions. For `n` cars traveling left to right and `n` cars traveling right to left, the total number of collisions is the number of ways to choose 2 cars from the total of `2n` cars. The number of ways to choose 2 cars from `2n` cars is given by the combination formula `2n * (2n - 1) / 2`.