```python
def car_race_collision(n: int):
    """
    Calculates the number of collisions in a car race where n cars are driving left to right 
    simultaneously, and another n cars are driving right to left at the same speed.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    return n * (n - 1)

# Test the function
print(car_race_collision(5))  # Output: 20
print(car_race_collision(10))  # Output: 90
```

This function works by treating each pair of cars as a unique collision. The number of pairs is given by the formula `n * (n - 1) / 2`, but since order doesn't matter and the cars in each direction are indistinguishable, we can simply use `n * (n - 1)`.