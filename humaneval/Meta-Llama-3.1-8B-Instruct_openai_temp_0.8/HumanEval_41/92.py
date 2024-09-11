```python
def car_race_collision(n: int):
    """
    This function calculates the number of car collisions in a car race scenario.
    
    Parameters:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of car collisions.
    """
    
    # The number of collisions is the sum of the first 'n' natural numbers
    # This is because for each car moving left to right, it can potentially collide with 'n-1' cars moving right to left
    # Therefore, the total number of collisions is the sum of 'n-1' for each car
    return n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This script defines a function `car_race_collision(n)` that takes an integer `n` as input, representing the number of cars in each direction. It calculates the number of potential collisions and returns the result. The calculation is based on the formula for the sum of the first `n-1` natural numbers, which is `n * (n - 1) // 2`. The script then provides example usage of the function with different input values.