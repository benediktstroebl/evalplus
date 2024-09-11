```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race with n cars
    moving left to right and n cars moving right to left.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    # Calculate the total number of collisions, which is the sum of the first n natural numbers
    collisions = n * (n + 1) // 2
    return collisions

# Test the function
print(car_race_collision(5))  # Output: 15
```

This script works because the number of collisions can be calculated by considering the pairs of cars that could collide. For each of the n cars moving left to right, there are n cars moving right to left that it could potentially collide with. Therefore, the total number of collisions is the sum of the first n natural numbers, which is given by the formula `n * (n + 1) / 2`.