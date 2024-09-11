```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race with n cars moving in opposite directions.

    Args:
    n (int): The number of cars moving in each direction.

    Returns:
    int: The number of collisions.
    """
    # The total number of pairs of cars is n * n (left to right cars vs right to left cars)
    # However, this counts each pair twice (car A vs car B and car B vs car A)
    # So we divide by 2 to get the correct number of unique pairs
    pair_count = n * n // 2
    
    # Each pair of cars collides once, so the number of collisions is equal to the number of pairs
    collision_count = pair_count
    
    return collision_count

# Example usage:
print(car_race_collision(5))  # Output: 10
```

However, this code can be simplified using the formula (n * (n - 1)) / 2. Here's how you can do it:

```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race with n cars moving in opposite directions.

    Args:
    n (int): The number of cars moving in each direction.

    Returns:
    int: The number of collisions.
    """
    # Using the formula for combinations (n * (n - 1)) / 2
    return n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
```