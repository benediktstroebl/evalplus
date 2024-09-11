```python
import math

def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions in a car race scenario.
    
    Args:
    n (int): The number of cars driving left to right and right to left.
    
    Returns:
    int: The number of collisions.
    """
    if n == 1:
        # If only one car is moving in each direction, there can't be any collisions
        return 0
    
    # Calculate the number of pairs of left-to-right and right-to-left cars
    pairs = math.comb(2 * n, 2)
    
    # For every pair, there's a 1/n chance of the left-to-right car being closest to the right-to-left car
    # This is because all n cars are equally spaced, and the probability of the left-to-right car being in any given position is 1/n
    # So, the expected number of collisions is (1/n) * (number of pairs)
    collision_expectation = (1/n) * pairs
    
    # However, the actual number of collisions is an integer, so we use the math.floor function to round down
    # This is because we can't have a fraction of a collision
    return math.floor(collision_expectation)

# Example usage:
print(car_race_collision(5))
```

This script uses the combination formula (math.comb) to calculate the number of pairs of left-to-right and right-to-left cars. It then uses the formula for expected value to calculate the expected number of collisions, and finally uses math.floor to round down to the nearest integer.