```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between two sets of cars,
    one moving left to right and the other right to left, on an infinitely long road.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The number of collisions.
    """
    return n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
```

In this code, we use the formula for combinations to calculate the number of pairs of cars, which is n*(n-1)/2. This is because each car in the left-to-right set can collide with each car in the right-to-left set, resulting in n*(n-1) possible collisions. Since we don't want to count each collision twice (once for each car), we divide by 2 to get the actual number of collisions.