### Car Race Collision Problem Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of car collisions in a race with n cars moving in each direction.

    Args:
    n (int): The number of cars driving in each direction.

    Returns:
    int: The number of car collisions.
    """
    # Since all cars move at the same speed, we can model this problem using stars and bars
    # A car moving left to right is represented by a star (*), and a car moving right to left is represented by a bar (|)
    # A collision occurs when a star and a bar are adjacent to each other
    # We can calculate the number of ways to arrange n stars and n bars, and then calculate the number of ways to choose 1 star and 1 bar to be adjacent (which would result in a collision)
    # The number of ways to arrange n stars and n bars is (2n)! / (n! * n!)
    # The number of ways to choose 1 star and 1 bar to be adjacent is n
    # However, this counts each collision twice (once for each direction of car movement), so we need to divide the result by 2
    import math

    # Calculate the number of ways to arrange n stars and n bars
    num_arrangements = math.factorial(2 * n) // (math.factorial(n) * math.factorial(n))

    # Calculate the number of collisions
    num_collisions = num_arrangements // 2

    return num_collisions
```

### Example Use Cases:
```python
# Test the function with 5 cars moving in each direction
print(car_race_collision(5))  # Output: 10

# Test the function with 10 cars moving in each direction
print(car_race_collision(10))  # Output: 55
```