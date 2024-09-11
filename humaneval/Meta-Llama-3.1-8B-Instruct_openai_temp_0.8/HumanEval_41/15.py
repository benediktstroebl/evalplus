```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario.
    
    Parameters:
    n (int): The number of cars in each direction.
    
    Returns:
    int: The total number of collisions.
    """
    
    # The number of collisions is equal to the sum of the first n-1 natural numbers
    # because each collision is a result of a unique pair of cars, and the order doesn't matter
    collisions = n * (n - 1) // 2
    
    return collisions

# Test the function
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This function uses the mathematical formula for the sum of the first n-1 natural numbers to calculate the number of collisions. The formula is `n * (n - 1) / 2`, which is derived from the fact that each number from 1 to n-1 contributes to the sum, and each number is added `n-1` times.