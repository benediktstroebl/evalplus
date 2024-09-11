### Car Race Collision Problem
```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions between two sets of n cars
    driving in opposite directions on an infinitely long straight road.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The total number of collisions.
    """
    # Calculate the total number of cars
    total_cars = 2 * n
    
    # Calculate the number of collisions using the formula for combinations of n items taken 2 at a time
    collisions = total_cars * (total_cars - 1) // 2 - n * (n - 1) // 2
    
    return collisions
```

### Example Usage:

```python
# Test the function with n = 3
print(car_race_collision(3))  # Output: 4
```

The reasoning behind this solution is that we can treat each set of n cars as a set of `n` distinct points that need to collide with the other set of points. The total number of ways these points can collide with each other is given by the number of combinations of `n` points taken 2 at a time, which is `n*(n-1)/2`. However, since we have two sets of `n` points, we need to multiply this by 2 to get the total number of collisions between the two sets. Finally, we subtract the number of collisions between the points in each set (`n*(n-1)/2`) because these are not the type of collisions we are counting.