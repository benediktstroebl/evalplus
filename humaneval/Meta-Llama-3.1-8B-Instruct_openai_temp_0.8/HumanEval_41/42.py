```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race scenario.

    Parameters:
    n (int): The number of cars driving left to right and the number of cars driving right to left.

    Returns:
    int: The number of collisions.
    """
    return n * (n - 1)
```

**Explanation**

The idea is to treat each left-to-right car as a potential colliding car, and each right-to-left car as a target car. Since a car can collide with every other car (except itself), we can use the formula for combinations to calculate the number of collisions.

However, in this case, since the order of the collisions doesn't matter (i.e., the fact that car A collides with car B is the same as car B colliding with car A), we can simply treat this as a combination problem without replacement, where we choose `n` items from a set of `n` items.

The formula for this is `n * (n - 1)`, which represents the number of ways to choose two items from a set of `n` items without replacement.

This formula assumes that each car can collide with every other car, and that the order of the collisions doesn't matter. It also assumes that the cars move in the same speed, and that the collisions don't affect the trajectory of the cars.

You can test this function with an example:
```python
print(car_race_collision(5))  # Output: 20
```