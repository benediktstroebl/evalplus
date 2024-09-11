### Car Collision Problem Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The total number of collisions.
    """
    # The number of pairs of cars that can collide is n * (n - 1) / 2 because each car in one group
    # can potentially collide with all cars in the other group except for itself.
    return n * (n - 1) // 2

# Test the function
if __name__ == "__main__":
    n = 5
    print(f"Number of collisions when n = {n}: {car_race_collision(n)}")
```

### Explanation
This problem is a classic example of combinatorics, specifically the concept of combinations. We can treat each pair of cars as a potential collision, and calculate the total number of such pairs.

The formula `n * (n - 1) / 2` is derived from the combination formula, which is used to calculate the number of ways to choose `k` items from a set of `n` items without regard to the order. In this case, we're choosing 2 cars from a set of `n` cars to collide.

The `//` operator is used for integer division to ensure that the result is an integer.