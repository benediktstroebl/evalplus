```python
import math

def car_race_collision(n: int):
    """
    Calculates the number of collisions in a straight line car race with n cars
    moving left to right and n cars moving right to left.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions.
    """
    # The number of collisions is equal to the sum of the first n-1 positive integers,
    # because each car moving left to right will collide with every car moving right to left
    # except for itself and the one immediately adjacent to it (on the left).
    collisions = n * (n - 1)
    
    # However, we have counted every collision twice, so we need to divide by 2.
    collisions //= 2
    
    return collisions

# Example usage:
n = 10
print(f"The number of collisions in a car race with {n} cars in each direction is: {car_race_collision(n)}")
```

This script uses the mathematical formula for the sum of the first n-1 positive integers to calculate the number of collisions in the car race, which is a well-known problem in combinatorics.