```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of car collisions.
    """
    # Initialize a list to store the positions of the left-to-right cars.
    right_cars = list(range(1, n + 1))

    # Initialize a variable to store the number of collisions.
    collisions = 0

    # Iterate over the positions of the right-to-left cars.
    for left_car in range(n, 0, -1):
        # Initialize a variable to store whether the current right-to-left car collides with any car.
        collides = False

        # Iterate over the positions of the left-to-right cars that are to the left of the current right-to-left car.
        for i, right_car in enumerate(right_cars):
            # If the current right-to-left car collides with the current left-to-right car, set collides to True and remove this car from the list.
            if left_car >= right_car:
                collides = True
                del right_cars[i]
                break

        # If the current right-to-left car collides with any car, increment the number of collisions.
        if collides:
            collisions += 1

    # Return the total number of collisions.
    return collisions

# Test the function with n = 5.
print(car_race_collision(5))
```

This script works by simulating the movement of the left-to-right cars and checking for collisions with the right-to-left cars. The positions of the left-to-right cars are stored in a list, and for each right-to-left car, it checks if it collides with any of the left-to-right cars that are to the left. If a collision is detected, the number of collisions is incremented and the left-to-right car is removed from the list. Finally, the total number of collisions is returned.