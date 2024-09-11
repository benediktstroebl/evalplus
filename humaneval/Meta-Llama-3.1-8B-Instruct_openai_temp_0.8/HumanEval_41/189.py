```python
def car_race_collision(n: int):
    """
    This function calculates the number of car collisions in a straight-line car race.

    Args:
    n (int): The number of cars driving in each direction.

    Returns:
    int: The number of car collisions.
    """
    def count_collisions(n):
        # The formula to calculate the number of collisions is n*(n-1)//2.
        # This is because we are choosing 2 cars out of n to collide, and the order
        # of these cars doesn't matter.
        return n*(n-1)//2

    return count_collisions(n)


# Example usage:
print(car_race_collision(5))  # Output: 10
```

This function uses the mathematical formula for the number of combinations of two items out of a set of `n` items. The number of collisions is equal to the number of ways to choose two cars out of the total number of cars in each direction.