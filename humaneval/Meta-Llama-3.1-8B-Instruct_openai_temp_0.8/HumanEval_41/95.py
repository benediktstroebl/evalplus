```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario.
    
    Parameters:
    n (int): The number of cars driving left to right and also the number of cars driving right to left.
    
    Returns:
    int: The total number of collisions.
    """
    return n * (n - 1) // 2

# Example usage:
n = 5
print(f"Number of collisions when {n} cars are racing: {car_race_collision(n)}")
```

This function uses the formula for combinations to calculate the number of collisions. The number of ways to choose two cars from a set of `n` cars is `n * (n - 1) / 2`, because you can choose the first car in `n` ways and the second car in `(n - 1)` ways, but you're counting each pair twice, so you divide by `2`.