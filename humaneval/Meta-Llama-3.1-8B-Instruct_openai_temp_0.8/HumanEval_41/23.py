```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between cars driving 
    left to right and right to left on an infinitely long straight road.

    Args:
        n (int): The number of cars driving left to right and right to left.

    Returns:
        int: The number of collisions between the two sets of cars.
    """
    # Initialize the total number of collisions
    total_collisions = 0
    
    # We can think of each car driving left to right as taking up a "space" on the road
    # because even though they don't physically collide, we want to count them as colliding
    # with the cars that are driving right to left
    for i in range(1, n + 1):
        # Each car driving left to right collides with every car driving right to left that is
        # farther down the road than it is, up to the nth car driving right to left
        total_collisions += min(n, i)
    
    # Since the total number of collisions is the sum of 1, 2,..., n, we can use the formula
    # n*(n+1)//2 to calculate it more efficiently
    return n * (n + 1) // 2


# Example usage:
print(car_race_collision(5))  # Output: 15
print(car_race_collision(10))  # Output: 55
```

This script works by iterating over each car driving left to right and counting the number of cars driving right to left that it collides with. However, this is inefficient for large numbers of cars. The formula `n * (n + 1) // 2` is used to calculate the total number of collisions more efficiently by using the formula for the sum of the first `n` positive integers.