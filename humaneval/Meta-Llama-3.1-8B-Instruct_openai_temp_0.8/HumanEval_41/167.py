```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race scenario.

    Args:
    n (int): The number of cars driving left to right and right to left.

    Returns:
    int: The number of collisions.
    """
    return n * (n - 1) // 2

# Test the function
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This function uses the formula for the number of combinations (n choose 2) to calculate the number of pairs of cars. Since each pair of cars that meet will collide, the total number of collisions will be the number of pairs.

However, the question already implies that a collision is counted for each pair of left to right and right to left cars. Therefore, the function just calculates n * (n - 1) / 2 which is the formula for n choose 2.

Note: In Python 3, the `//` operator is used for integer division, which returns the quotient as an integer. This is used to avoid a floating-point result.