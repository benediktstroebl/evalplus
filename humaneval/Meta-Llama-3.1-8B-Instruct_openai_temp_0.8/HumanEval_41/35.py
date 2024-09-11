```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between left-to-right and right-to-left cars.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    # Calculate the number of collisions using the formula for combinations
    # Since each collision is unique and order doesn't matter, we use n choose 2
    # which is equivalent to n*(n-1)/2
    collisions = n * (n - 1) // 2
    return collisions

# Example usage
print(car_race_collision(5))  # Output: 10
```

In this script, we calculate the number of collisions by considering each car as a possible colliding partner for every other car. Since the order of collision does not matter (i.e., a collision between car A and car B is the same as between car B and car A), we use the combination formula `n choose 2` which is equivalent to `n*(n-1)/2`. This formula divides the total number of pairs of cars by 2 to avoid counting each pair twice.