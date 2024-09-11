```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario
    where n cars are driving left to right and n cars are driving right to left.

    Args:
    n (int): The number of cars driving left to right.

    Returns:
    int: The number of collisions.
    """
    return n * (n - 1) // 2

# Test the function
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This function uses the formula for the sum of an arithmetic series, specifically the sum of the first n natural numbers, which is `n * (n - 1) / 2`. In this case, the number of possible collisions is equal to the number of pairs of cars that can collide, which is `n * (n - 1) / 2`.