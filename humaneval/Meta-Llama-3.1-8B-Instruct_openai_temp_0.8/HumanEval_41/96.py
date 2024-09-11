```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race where n cars move left to right
    and n cars move right to left.

    Args:
        n (int): The number of cars moving in each direction.

    Returns:
        int: The total number of collisions.
    """
    # Initialize the total number of collisions to 0
    total_collisions = 0

    # Since the cars are moving at the same speed, a collision occurs when two cars meet
    # We can model this as a sequence of pairs of numbers from 1 to n, where the first
    # number represents the position of a car moving left to right and the second number
    # represents the position of a car moving right to left.
    for i in range(1, n + 1):
        # For each car moving left to right, we need to check for collisions with all
        # cars moving right to left.
        for j in range(1, n + 1):
            # A collision occurs if i (left-to-right car) is equal to n + 1 - j (right-to-left car)
            if i == n + 1 - j:
                # Increment the total number of collisions
                total_collisions += 1

    # Return the total number of collisions
    return total_collisions


# Test the function with a sample input
print(car_race_collision(5))
```

This script defines a function `car_race_collision(n)` that calculates the number of collisions in a car race with `n` cars moving left to right and `n` cars moving right to left. The function uses two nested loops to iterate over all possible pairs of cars and checks for collisions by comparing their positions. The total number of collisions is then returned.

When you run this script with the sample input `car_race_collision(5)`, it will output the total number of collisions for that scenario.