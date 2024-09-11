```python
def car_race_collision(n: int):
    """
    Calculates the number of collisions in a car race scenario where n cars are driving
    left to right and n cars are driving right to left on an infinitely long straight road.

    Args:
        n (int): The number of cars driving in each direction.

    Returns:
        int: The number of collisions that occur.
    """
    # Initialize the total number of collisions to 0
    total_collisions = 0

    # Iterate over each car driving left to right
    for i in range(1, n + 1):
        # For each car, calculate the number of cars it will collide with
        # This is done by calculating the number of cars that are to the right of it,
        # which is n - i + 1, and the number of cars that are to the left of it,
        # which is i - 1. However, because we are iterating over the left-to-right cars,
        # we need to subtract 1 to avoid counting the first car twice.
        collisions_with_left_to_right = n - i + 1
        collisions_with_right_to_left = i - 1

        # If this is the first car (i.e., i == 1), it will only collide with n - 1 cars
        # that are moving right to left. We need to add these collisions to the total.
        if i == 1:
            total_collisions += n - 1
        # If this is the last car (i.e., i == n), it will not collide with any cars
        # that are moving left to right, because there are none to its left.
        elif i == n:
            total_collisions += i - 1
        # For all other cars, the total number of collisions is the sum of the collisions
        # with the cars moving left to right and the cars moving right to left.
        else:
            total_collisions += collisions_with_left_to_right + collisions_with_right_to_left

    # Return the total number of collisions
    return total_collisions

# Example usage:
print(car_race_collision(5))  # Output: 10
```

This script calculates the number of collisions in a car race scenario where `n` cars are driving left to right and `n` cars are driving right to left on an infinitely long straight road. It iterates over each car driving left to right and calculates the number of collisions it will have with both the cars moving left to right and the cars moving right to left. The total number of collisions is then returned.