```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario.
    
    Args:
    n (int): The number of cars moving left to right and right to left.
    
    Returns:
    int: The total number of collisions.
    """
    
    # Calculate the number of collisions using the formula n*(n-1)//2
    # This is derived from the fact that each pair of cars collides once
    # and there are n*(n-1)//2 unique pairs of cars
    return n * (n - 1) // 2

# Example usage:
n = 5
print(f"The number of collisions when there are {n} cars moving left to right and {n} cars moving right to left is: {car_race_collision(n)}")
```

This script defines a function `car_race_collision` that takes the number of cars `n` as an argument and returns the number of collisions. The function uses the formula `n*(n-1)//2` to calculate the number of collisions, which is derived from the fact that each pair of cars collides once. The example usage demonstrates how to call the function with a specific value for `n` and print the result.