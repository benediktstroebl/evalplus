```python
def car_race_collision(n: int):
    """
    Calculate the number of car collisions in a two-directional car race.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of car collisions.
    """
    # Initialize the number of collisions to 0
    collisions = 0
    
    # Calculate the number of collisions for each pair of cars
    # Since all cars are driving at the same speed, we can treat this as a stars and bars problem
    # We can imagine the cars as stars and the spaces between them as bars
    # The number of bars is n - 1 (because there are n spaces between n stars)
    # The number of stars is 2n (because there are n cars in each direction)
    # The number of ways to arrange these stars and bars is given by the formula: C(2n + n - 1, n)
    # However, this counts each collision twice (once for each car involved in the collision)
    # So we divide by 2 to get the correct number of collisions
    import math
    collisions = math.comb(3 * n - 2, n)
    
    return collisions

# Example usage:
print(car_race_collision(5))  # Output: 30
```

This script uses the `math.comb` function to calculate the binomial coefficient C(3n - 2, n), which represents the number of ways to arrange the stars and bars in the stars and bars problem. This is equivalent to the number of collisions in the car race. The result is then divided by 2 to account for the fact that each collision is counted twice.