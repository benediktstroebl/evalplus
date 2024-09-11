```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    return (n * (n - 1)) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
print(car_race_collision(20))  # Output: 190
```

This function uses the formula for combinations (nCr) to calculate the number of collisions, where n is the total number of cars and r is half of the total number of cars. In this case, r is (n - 1) because each of the n cars has a distinct collision with each of the other n - 1 cars.

When there are n cars, the formula for nCr can be simplified to n * (n - 1) / 2, which is the number of collisions. This function uses integer division // to ensure that the result is an integer, even when the input is large.