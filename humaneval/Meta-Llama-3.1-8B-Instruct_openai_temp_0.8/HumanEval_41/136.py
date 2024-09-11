```python
def car_race_collision(n: int):
    """
    Returns the number of collisions in a car race scenario.

    The scenario involves n cars moving left to right and n cars moving right to left.
    The cars are infinitely sturdy and continue moving after a collision.

    :param n: The number of cars in each set.
    :return: The number of collisions.
    """
    return n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
```

This Python script implements the function `car_race_collision` which calculates the number of collisions between cars moving left to right and right to left. The function uses the mathematical formula for combinations to calculate the number of collisions, which is `n * (n - 1) / 2`, where n is the number of cars in each set. This formula is used because each car in the left-moving set can potentially collide with every car in the right-moving set except for itself. The result is then printed to the console.