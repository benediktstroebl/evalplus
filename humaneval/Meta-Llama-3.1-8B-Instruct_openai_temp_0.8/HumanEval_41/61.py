### Car Collision Simulator
```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of car collisions in a straight infinite road.
    
    Parameters:
    n (int): The number of cars moving left to right and right to left.

    Returns:
    int: The number of car collisions.
    """
    # Initialize a list to store the positions of the cars moving left to right
    left_cars = [i for i in range(1, n + 1)]
    
    # Initialize a list to store the positions of the cars moving right to left
    right_cars = [i for i in range(n, 1, -1)]
    
    # Initialize a counter to store the number of collisions
    collisions = 0
    
    # Iterate over the positions of the cars moving left to right
    for i in range(len(left_cars)):
        # Check for collisions with the cars moving right to left
        for j in range(len(right_cars)):
            # If the cars are at the same position, increment the collision counter
            if left_cars[i] == right_cars[j]:
                collisions += 1
    
    # Return the total number of collisions
    return collisions


# Example usage:
n = 5
print(f"Number of collisions for {n} cars: {car_race_collision(n)}")
```

This script simulates the car collision scenario by creating two lists, one for each set of cars. It then iterates over the positions of the cars moving left to right and checks for collisions with the cars moving right to left. The number of collisions is incremented each time a collision is detected, and the total count is returned at the end.