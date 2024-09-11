```python
def car_race_collision(n: int) -> int:
    """
    This function returns the number of collisions in a car race scenario where
    two sets of n cars drive in opposite directions.

    The function uses the concept that the number of collisions is equal to the sum
    of the first n-1 positive integers. This is because each pair of cars will
    collide once.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    return n * (n - 1) // 2

# Test the function
print(car_race_collision(5))  # Output: 10
```

In this code, we use the formula for the sum of the first `n-1` positive integers, which is `n * (n - 1) / 2`. This formula is derived from the fact that each pair of cars will collide once.