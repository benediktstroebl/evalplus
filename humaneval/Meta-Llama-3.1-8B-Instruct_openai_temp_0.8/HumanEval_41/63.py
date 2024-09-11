```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between two sets of n cars 
    moving in opposite directions on a straight road. The cars are infinitely sturdy 
    and will continue moving without any change in velocity after a collision.
    
    Parameters:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions that will occur.
    """
    # The total number of cars is 2n, and they are moving at a constant speed.
    # For each car moving to the right, there are n-1 cars moving to the left that 
    # it can potentially collide with. This gives us a total of n(n-1) collisions.
    # However, this counts each collision twice because each car is counted on both 
    # sides of the collision, so we divide by 2 to get the actual number of collisions.
    # Since there are two sets of n cars, we multiply the result by 2.
    return 2 * n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 20
```

This script defines a function `car_race_collision` that calculates the total number of collisions between two sets of `n` cars moving in opposite directions. The function uses the formula `2 * n * (n - 1) // 2` to calculate the number of collisions, which is based on the fact that each car moving to the right can collide with `n-1` cars moving to the left, and each collision is counted twice. The result is then printed for an example usage with `n = 5`.