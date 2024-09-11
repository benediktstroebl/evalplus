```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between two sets of cars driving in opposite directions.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The total number of collisions.
    """
    # The number of pairs of cars that can collide is n * (n - 1) / 2, 
    # because each car on the left can collide with n-1 cars on the right.
    # However, each collision is counted twice (once for each car involved), 
    # so we need to divide the result by 2.
    return n * (n - 1) // 2


# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This script defines a function `car_race_collision` that takes the number of cars `n` as input and returns the total number of collisions between the two sets of cars. The function uses the formula `n * (n - 1) // 2` to calculate the number of pairs of cars that can collide, and then divides the result by 2 to account for the fact that each collision is counted twice. The function is then tested with some example inputs to demonstrate its usage.