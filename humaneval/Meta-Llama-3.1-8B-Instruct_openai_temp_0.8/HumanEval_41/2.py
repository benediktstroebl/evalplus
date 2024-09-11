```python
def car_race_collision(n: int):
    """
    Calculate the number of car collisions in a car race scenario.

    Args:
    n (int): The number of cars driving left to right and right to left.

    Returns:
    int: The total number of car collisions.
    """
    return n * (n - 1)

# Example usage:
print(car_race_collision(5))  # Output: 20
```
This script uses the formula for combinations to calculate the number of collisions. Each car driving left to right will collide with each car driving right to left, hence `n * (n - 1)`.