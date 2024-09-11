```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions for 'n' cars.

    Args:
        n (int): The number of cars on each side.

    Returns:
        int: The total number of collisions.
    """
    # Since all cars move at the same speed, 
    # the time it takes for the first car to collide with the second is the same 
    # as the time it takes for the first car to collide with the nth car.
    # Therefore, the number of collisions is the sum of the first 'n' natural numbers.

    return n * (n - 1) // 2

# Test the function
print(car_race_collision(5))
```

This script uses the formula for the sum of the first 'n' natural numbers to efficiently calculate the total number of collisions. It simply returns the result of the formula, which is `n * (n - 1) / 2`.