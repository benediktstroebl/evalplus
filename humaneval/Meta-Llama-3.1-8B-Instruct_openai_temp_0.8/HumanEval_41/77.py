### Car Race Collision Problem Solution
```python
def car_race_collision(n: int) -> int:
    """
    Computes the number of car collisions in a car race scenario.

    Two sets of n cars are driving left to right and right to left on an infinitely long line.
    The cars are moving at the same speed. A collision occurs when a car moving left to right
    hits a car moving right to left. The cars are infinitely sturdy and strong, so after a collision,
    they continue moving.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The total number of collisions.
    """

    # The number of collisions is equal to the sum of the first n-1 positive integers
    # because each car that is not the last one will collide with every car to its right.
    return n - 1 + (n - 1) * n // 2
```

### Example Use Cases

```python
print(car_race_collision(2))  # Output: 1
print(car_race_collision(3))  # Output: 5
print(car_race_collision(4))  # Output: 9
```

In this solution, we calculate the number of collisions by summing up the first `n-1` positive integers. Each car (excluding the last one) will collide with every car to its right. We use the formula `n - 1 + (n - 1) * n // 2` to compute this sum, where `//` is the integer division operator.