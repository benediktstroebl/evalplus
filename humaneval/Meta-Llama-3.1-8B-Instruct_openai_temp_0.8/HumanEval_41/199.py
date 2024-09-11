## Car Race Collision Problem
### Description
The `car_race_collision` function calculates the number of collisions between two sets of `n` cars moving in opposite directions on an infinite straight line. The cars move at the same speed and are infinitely sturdy, causing them to continue moving after collision.

### Solution

```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions.
    """
    return n * (n - 1)
```

### Explanation
Since each car from the left-moving set can collide with every car from the right-moving set except itself, the number of potential collisions is `n * n`. However, we must subtract `n * n` to exclude the cases where a car collides with itself, because cars cannot collide with themselves. This leaves us with `n * (n - 1)` potential collisions.