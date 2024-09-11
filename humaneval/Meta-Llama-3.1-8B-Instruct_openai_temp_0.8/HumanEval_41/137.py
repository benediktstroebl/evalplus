### Car Race Collision Solution
```python
def car_race_collision(n: int) -> int:
    """
    Returns the number of collisions in a car race scenario.

    In this scenario, n cars are driving left to right and n cars are driving right to left.
    All cars move at the same speed. Two cars collide when a left to right car hits a right to left car.
    However, the cars are infinitely sturdy and continue moving in their trajectory.

    Args:
        n (int): The number of cars driving left to right and right to left.

    Returns:
        int: The number of collisions in the scenario.
    """

    # The number of collisions is equal to the number of pairs of cars.
    # This is equivalent to the number of pairs of elements in a set of n elements.
    # We can calculate this using the combination formula: n choose 2 = n * (n - 1) / 2
    return n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```
This script uses the mathematical formula for combinations (n choose 2) to calculate the number of collisions in the car race scenario. The formula is `n * (n - 1) / 2`, where `n` is the number of cars. The `//` operator is used for integer division to ensure that the result is an integer.