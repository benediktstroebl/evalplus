```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car racing scenario.
    
    Parameters:
    n (int): The number of cars in each direction.
    
    Returns:
    int: The total number of collisions.
    """
    
    # Initialize the collision count to 0
    collisions = 0
    
    # The number of unique pairs of cars that can collide is equal to the sum of the first (n-1) positive integers
    # We use the formula n*(n-1) // 2 to calculate the sum
    collisions = n * (n - 1) // 2
    
    # Return the total number of collisions
    return collisions

# Example usage
n = 10
print(f"The number of collisions when there are {n} cars in each direction is: {car_race_collision(n)}")
```

This script uses the formula for the sum of the first (n-1) positive integers, which is `n*(n-1) // 2`, to calculate the number of unique pairs of cars that can collide. The `//` operator is used for integer division to ensure that the result is an integer.