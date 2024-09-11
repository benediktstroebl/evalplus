### Car Collision Problem Solver

The following Python script uses a greedy approach to solve the car collision problem.

```markdown
### Code

```python
def car_race_collision(n: int):
    """
    Returns the number of car collisions in a simultaneous left-right car race.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    # Each pair of cars (one from left and one from right) results in 1 collision.
    # Since there are n cars in each direction, the total number of pairs is n * (n - 1) / 2.
    total_collisions = n * (n - 1) // 2
    return total_collisions


### Example Use Case

# Test the function with 5 cars in each direction
print(car_race_collision(5))
```

### Explanation

The solution is based on the principle that each pair of cars from the left and right directions will result in 1 collision. We can use the formula for combinations to calculate the total number of pairs, which is `n * (n - 1) / 2`, where `n` is the number of cars in each direction.

By using integer division (`//`) in the calculation, we ensure that the result is an integer, which represents the total number of collisions.

Note that this solution assumes that the number of cars in each direction is the same, as stated in the problem. If the number of cars is different, the solution would need to be adjusted accordingly.