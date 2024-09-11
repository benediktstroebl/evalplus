```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between two sets of n cars,
    one moving left to right and the other moving right to left on a straight road.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions.
    """
    # The number of collisions is equal to the sum of the number of pairings 
    # between the cars moving left to right and the cars moving right to left.
    # This is equivalent to the number of pairings between n cars and n cars,
    # which is n choose 2 (or n*(n-1)/2). However, since we have two sets of n cars,
    # we need to multiply this by 2.
    total_collisions = n * (n - 1) // 2 * 2
    
    return total_collisions

# Example usage:
print(car_race_collision(5))  # Output: 20
```

This function uses the formula for combinations (n choose k) to calculate the number of pairings between the cars. Since there are two sets of cars, the total number of collisions is twice this value. The `//` operator is used for integer division, ensuring that the result is an integer.