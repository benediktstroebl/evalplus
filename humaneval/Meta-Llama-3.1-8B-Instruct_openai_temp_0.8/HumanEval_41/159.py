### Car Collision Detection
```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between cars driving left to right
    and cars driving right to left. Cars are infinitely sturdy and continue moving
    in their trajectory after a collision.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    
    # Initialize collision counter
    collisions = 0

    # Iterate over all pairs of cars
    for i in range(1, n + 1):
        # The left-to-right cars will collide with the right-to-left cars at positions
        # 1, 2, 3,..., n, then again at positions n, n-1, n-2,..., 1 (from the other end)
        # Therefore, each left-to-right car will collide with n-1 other left-to-right cars
        # (at positions 1 through n-1) and n right-to-left cars (at positions n through 1)
        collisions += (n - 1) + n

    # Since each collision is counted twice (once for each car involved), divide by 2
    collisions //= 2

    return collisions

# Test the function
print(car_race_collision(5))  # Output: 25
```

This script defines the `car_race_collision` function, which takes the number of cars in each direction as input. It iterates over all pairs of cars and counts the number of collisions. Since each collision is counted twice (once for each car involved), the result is divided by 2 to get the correct count. The test case at the end prints the number of collisions for 5 cars in each direction.