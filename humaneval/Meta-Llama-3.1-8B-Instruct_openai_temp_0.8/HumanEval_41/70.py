```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario.
    
    Args:
    n (int): The number of cars driving in each direction.

    Returns:
    int: The number of collisions that occur.
    """
    # The formula to calculate the number of collisions is (n * (n-1)) / 2
    # This is because each of the n cars collides with (n-1) other cars
    # We divide by 2 because each collision is counted twice (once for each car involved)
    return n * (n-1) // 2

# Test the function
print(car_race_collision(5))
```

This script defines a function `car_race_collision` that takes an integer `n` as input and returns the number of collisions that occur. The formula used to calculate the number of collisions is derived from combinatorics and is based on the fact that each of the `n` cars collides with `n-1` other cars, but each collision is counted twice. The script then tests the function with `n = 5`.