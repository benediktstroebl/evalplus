```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.

    Args:
        n (int): The number of cars moving in each direction.

    Returns:
        int: The total number of collisions.
    """
    # Two cars can collide if and only if they have different 'positions' in the sequence {1, 2,..., n, n, n-1,..., 1}
    # A position of 1 means the car is moving from left to right, and a position of n means it's moving from right to left
    # We can calculate the number of collisions using the formula for triangular numbers: n*(n+1)//2
    return n * (n + 1) // 2

# Test the function
n = 5
print(f"The number of collisions between {n} cars moving in each direction is: {car_race_collision(n)}")
```

When you run this script, it will calculate and print the number of collisions between `n` cars moving in each direction. The formula `n * (n + 1) // 2` is derived from the fact that for each car moving left to right, there are `n - 1` cars moving right to left that it can collide with, resulting in a total of `n * (n - 1)` collisions. However, since each collision is counted twice (once for each car involved), we divide by `2` to get the correct count.