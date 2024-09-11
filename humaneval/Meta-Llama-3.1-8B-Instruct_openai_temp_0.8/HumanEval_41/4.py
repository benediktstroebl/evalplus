```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions in a car race scenario.
    
    Parameters:
    n (int): The number of cars in each direction.
    
    Returns:
    int: The number of collisions.
    """
    # The number of collisions is equal to the sum of the first n positive integers
    # This is because each car that is moving left to right will collide with each car that is moving right to left
    # The formula for the sum of the first n positive integers is n*(n+1)/2
    return n * (n + 1) // 2

# Example usage
print(car_race_collision(5))  # Output: 15
```

This script defines a function `car_race_collision` that takes an integer `n` as input and returns the number of collisions in the car race scenario. The function uses the formula for the sum of the first `n` positive integers to calculate the number of collisions. The example usage at the end of the script shows how to call the function with `n = 5` and print the result.