```python
def car_race_collision(n: int):
    """
    Returns the number of collisions in a car racing scenario.

    Args:
        n (int): The number of cars driving left to right and right to left.

    Returns:
        int: The number of collisions.
    """
    return n * (n - 1) // 2

# Example use case:
print(car_race_collision(5))  # Output: 10
```

Explanation:
To calculate the number of collisions in the given scenario, we can treat each pair of cars as a potential collision. For `n` cars on each side, there are `n * n` possible pairs. However, each pair is counted twice (once for each car), so we divide by 2.

Using the formula `n * (n - 1) // 2` gives us the correct number of collisions, where `//` is used for integer division to ensure the result is an integer.

This solution assumes that the cars are distinguishable and that collisions are only between cars from the two sets, not between cars within the same set.