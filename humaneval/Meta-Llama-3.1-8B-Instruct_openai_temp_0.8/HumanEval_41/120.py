```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between left-to-right and right-to-left cars.
    
    :param n: The number of cars in each direction.
    :return: The number of collisions.
    """
    # Initialize the number of collisions
    collisions = 0
    
    # Calculate the number of pairs of cars that can collide
    # Since the cars move in the same speed, all pairs of cars from left and right will collide
    # The maximum number of pairs for left cars is n-1 (it can't collide with itself)
    # So the total number of pairs is the number of left cars times the number of right cars
    # We can use the formula for combination to calculate this: n choose 2
    import math
    collisions = math.comb(n, 2)
    
    # Return the number of collisions
    return collisions

# Test the function
print(car_race_collision(5))
```

This script defines the function `car_race_collision` that calculates the number of collisions between left-to-right and right-to-left cars. It uses the `math.comb` function to calculate the number of pairs of cars that can collide, then returns this value.

Note that `math.comb` is available in Python 3.8 and later versions. If you are using an earlier version, you can use the following formula instead:

```python
collisions = n * (n - 1) // 2
```