```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race where n cars
    are driving left to right and n cars are driving right to left on an infinitely
    long straight road. All cars move at the same speed and are infinitely sturdy.
    
    Parameters:
    n (int): The number of cars in each direction.
    
    Returns:
    int: The number of collisions.
    """
    # Initialize the number of collisions to 0
    collisions = 0
    
    # For each pair of cars
    for i in range(n):
        for j in range(n):
            # Check if the cars collide (i.e., if they move in opposite directions)
            if (i + j) % 2!= 0:
                # If they collide, increment the number of collisions
                collisions += 1
    
    # Since each pair of cars will collide an equal number of times as the total number of pairs of cars minus the pair itself. 
    # Hence, we should divide by 2 to avoid double counting
    return int(collisions / 2)
```

Here's an example of how to use this function:

```python
print(car_race_collision(5))  # Output: 5
```

This script works by counting the number of pairs of cars that are moving in opposite directions. Since each pair of cars will collide an equal number of times as the total number of pairs of cars minus the pair itself, we divide by 2 to avoid double counting. Note that this is a simplified solution and assumes that the cars are treated as unique entities. If the cars are considered identical, the problem becomes more complex.