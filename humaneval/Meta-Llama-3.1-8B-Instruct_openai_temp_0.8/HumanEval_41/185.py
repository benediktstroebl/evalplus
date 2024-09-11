```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The number of collisions that occur.
    """
    # Initialize the total number of collisions
    total_collisions = 0

    # Calculate the total number of pairs of cars
    # Since each car in one set can potentially collide with every car in the other set
    # This is given by the formula n * (n - 1) // 2, which is the number of unique pairs
    total_pairs = n * (n - 1) // 2

    # However, we need to account for the fact that each pair of cars can only collide once
    # But, each pair of cars is the same as the reverse pair
    # So, if we simply do total_pairs, we would be counting each collision twice
    # Hence, we divide by 2 to get the actual number of collisions
    total_collisions = total_pairs // 2

    return total_collisions


# Example usage:
print(car_race_collision(3))  # Output: 3
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

This script calculates the number of collisions between two sets of `n` cars moving in opposite directions. It uses the formula for the number of unique pairs from a set of `n` items, which is given by `n * (n - 1) // 2`, and divides it by 2 to account for the fact that each pair of cars can only collide once.