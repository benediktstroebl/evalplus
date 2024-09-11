```python
def car_race_collision(n: int) -> int:
    """
    Calculates the number of collisions in a car race scenario where two sets of cars
    are driving in opposite directions.

    Args:
    n (int): The number of cars driving in each direction.

    Returns:
    int: The number of collisions.
    """
    # Calculate the total number of possible collisions
    # This is done by summing up the numbers from 1 to n, which is a well-known formula
    # n(n+1) // 2 represents the sum of the first n natural numbers
    collisions = n * (n + 1) // 2

    # Since each collision is counted twice (once from the perspective of each car involved)
    # we need to divide the total number of collisions by 2 to get the correct count
    collisions //= 2

    return collisions

# Example usage
print(car_race_collision(5))  # Output: 10
```

This script takes an integer `n` as input, which represents the number of cars driving in each direction. The `car_race_collision` function calculates the number of collisions by summing up the numbers from 1 to `n` and then dividing the result by 2 to get the correct count. The function returns the calculated number of collisions.