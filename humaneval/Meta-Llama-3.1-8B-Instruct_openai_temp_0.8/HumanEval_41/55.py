```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The number of collisions.
    """
    # The formula for the number of collisions is n * n - n
    # This is because each pair of cars can collide, but we subtract n because
    # each car can collide with itself, which is not a valid collision
    return n * n - n

# Example usage:
print(car_race_collision(5))  # Output: 20
```

This script defines a function `car_race_collision` that takes the number of cars in each set as input and returns the number of collisions. The function uses a simple mathematical formula to calculate the number of collisions, which is `n * n - n`, where `n` is the number of cars in each set. The example usage at the end demonstrates how to call the function with a specific input and print the result.