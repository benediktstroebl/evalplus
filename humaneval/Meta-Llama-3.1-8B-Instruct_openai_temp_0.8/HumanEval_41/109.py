```python
import itertools

def car_race_collision(n: int) -> int:
    """
    Calculate the number of car collisions in a simultaneous car race.

    Args:
        n (int): The number of cars moving left to right and right to left.

    Returns:
        int: The total number of car collisions.
    """
    
    # Initialize a counter for collisions
    collisions = 0
    
    # Generate pairs of cars moving left to right and right to left
    left_to_right = list(range(n))
    right_to_left = list(range(n))
    
    # Use itertools.product to get all possible pairs of cars
    for left, right in itertools.product(left_to_right, right_to_left):
        
        # Two cars cannot collide if they are the same car
        if left!= right:
            # Increment the collision count only if the cars are at the same position
            collisions += 1
    
    # Return the total number of collisions divided by 2, since each collision is counted twice
    return collisions // 2
```

This script defines a function `car_race_collision(n)` that takes the number of cars as input and returns the total number of car collisions. It uses the `itertools.product` function to generate all possible pairs of cars, checks for collisions, and returns the total count of collisions divided by 2 to avoid counting each collision twice.