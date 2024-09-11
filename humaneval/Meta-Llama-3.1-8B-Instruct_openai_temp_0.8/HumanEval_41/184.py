```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between n cars moving left to right
    and n cars moving right to left on an infinitely long straight road.

    The number of collisions is equivalent to the sum of the first n natural numbers,
    which can be calculated using the formula: n*(n+1)//2

    Args:
        n (int): The number of cars moving left to right (or right to left).

    Returns:
        int: The number of collisions.
    """
    return n*(n+1)//2

# Example usage:
print(car_race_collision(5))  # Output: 15
```

In this script, we use the mathematical formula for the sum of an arithmetic series to calculate the number of collisions. The formula `n*(n+1)//2` calculates the sum of the first `n` natural numbers, which corresponds to the number of collisions in this problem.