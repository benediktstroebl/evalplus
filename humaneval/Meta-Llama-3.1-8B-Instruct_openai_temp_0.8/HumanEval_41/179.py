```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between cars moving left to right
    and cars moving right to left in a straight infinitely long road.

    Args:
        n (int): The number of cars moving left to right and right to left.

    Returns:
        int: The number of collisions.
    """
    # Calculate the total number of cars
    total_cars = n * 2
    
    # Calculate the number of collisions
    # Since each pair of cars from different directions will collide once, we can use the combination formula
    # The number of pairs is equal to the number of cars from one direction times the number of cars from the other direction
    # We use the math.comb function to calculate the combination
    import math
    collisions = math.comb(n, 2)
    
    return collisions

# Test the function
print(car_race_collision(10))  # Output: 45
```

In this script, we use the combination formula to calculate the number of pairs of cars from different directions that will collide. The `math.comb` function is used to calculate the combination of `n` items taken `k` at a time, which is defined as `n! / (k! * (n-k)!)`. In this case, `n` is the number of cars from one direction and `k` is 2, so we calculate the number of pairs of cars from different directions.