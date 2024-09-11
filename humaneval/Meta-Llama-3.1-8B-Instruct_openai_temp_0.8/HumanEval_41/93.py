```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race scenario.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The total number of collisions.
    """
    # The number of collisions is equal to the sum of the first n-1 positive integers
    # This is because the first car in each direction will not collide, so we start
    # from the second car, and for each car, it will collide with all the cars
    # that are moving in the opposite direction that it hasn't collided with yet
    collisions = n * (n - 1) // 2

    return collisions

# Example usage:
print(car_race_collision(5))
```

This script uses the formula for the sum of the first n-1 positive integers to calculate the number of collisions, which occurs when each car moving left to right collides with all the cars moving right to left that it hasn't collided with yet. 

For example, if there are 5 cars moving left to right and 5 cars moving right to left, the first car moving left to right will not collide with any cars, the second car will collide with 4 cars, the third car will collide with 3 cars, the fourth car will collide with 2 cars, and the fifth car will collide with 1 car. Therefore, the total number of collisions is (4 + 3 + 2 + 1) = 10. 

Note that this formula can be derived by recognizing that each car moving left to right will collide with all the cars moving right to left except itself, and that each car moving right to left will collide with all the cars moving left to right except itself. Therefore, the total number of collisions is equal to the sum of the first n-1 positive integers.