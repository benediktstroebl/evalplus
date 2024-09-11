```python
def car_race_collision(n: int) -> int:
    """
    Calculates the number of collisions in a car race scenario.
    
    This function takes into account that the cars are infinitely sturdy and strong.
    It uses the concept of a "flight" of n cars, where a flight is a sequence of
    n cars with each car having a unique trajectory. The number of possible
    collisions between two flights is the sum of the first n-1 integers.
    
    Args:
        n (int): The number of cars in a flight.
    
    Returns:
        int: The number of collisions.
    """
    # Calculate the sum of the first n-1 integers using the formula: n*(n-1)/2
    # This is a simplification of the problem since the cars are infinitely sturdy
    # and the order of collisions doesn't matter
    collisions = (n * (n - 1)) // 2
    
    return collisions

# Example usage:
print(car_race_collision(5))  # Output: 10
```

This script defines a function `car_race_collision` that calculates the number of collisions in a car race scenario. It uses the concept of a "flight" of `n` cars and calculates the sum of the first `n-1` integers to determine the number of possible collisions between two flights. The function takes an integer `n` as input and returns the number of collisions. The script also includes an example usage of the function.