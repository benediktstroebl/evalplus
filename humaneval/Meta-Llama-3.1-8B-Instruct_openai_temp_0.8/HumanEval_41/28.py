```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between two sets of cars moving 
    in opposite directions on an infinitely long straight road.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions.
    """
    total_collisions = 0

    # Calculate total pairs of cars
    total_pairs = n * (n - 1) // 2
    
    # Each pair of cars can collide one time, except for the last (n-1) pairs in each set.
    # The last (n-1) pairs in each set can collide (n-1) times, but the last car in each set
    # can not collide with any car in the other set.
    total_collisions = total_pairs - (n - 1)

    return total_collisions

# Example usage:
n = 5
print(f"The number of collisions when n = {n} is: {car_race_collision(n)}")
```

This script works by calculating the total number of pairs of cars using the formula for combinations (nC2), and then subtracting the number of pairs that cannot collide (i.e., the last n-1 pairs in each set). The result is the total number of collisions that can occur.