### Car Collision Problem Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of car collisions in a straight road with n cars driving left to right
    and n cars driving right to left, all moving at the same speed.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The total number of car collisions.
    """
    return n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
```
In this solution, we use the concept of combinations to calculate the number of collisions. Each pair of cars can potentially collide, and since we have `n` cars in each direction, we can pair them up in `n * (n - 1) / 2` ways. This formula represents the number of combinations of `n` items taken 2 at a time, which is the number of unique pairs of cars that can collide.