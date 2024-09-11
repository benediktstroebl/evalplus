```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions between two sets of n cars 
    moving in opposite directions on an infinitely long straight road.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions between the cars.
    """
    # The number of collision pairs is equal to the number of combinations of n cars taken 2 at a time
    # This is because for each pair of cars, there will be one collision (regardless of the order of the pair)
    # We use the formula for combinations: n choose 2 = n * (n - 1) / 2
    return n * (n - 1) // 2

# Test the function
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This script defines a function `car_race_collision` that takes the number of cars in each set as input and returns the total number of collisions. The function uses the formula for combinations to calculate the number of collision pairs, which is the total number of collisions. The script then tests the function with example inputs.