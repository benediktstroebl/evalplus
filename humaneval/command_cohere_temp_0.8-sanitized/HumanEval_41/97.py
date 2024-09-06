def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move toward each other on an infinitely long straight road.

    Args:
        n (int): Number of cars in each set.

    Returns:
        int: The number of collisions between the moving cars.
    """
    # Define the two sets of cars as two lists that represent the cars moving from left to right and right to left respectively.
    cars1, cars2 = [], []
    # Initialize trackers for left and right pointers
    i, j = 0, 0
    # Initialize a counter for collisions
    collision_count = 0

    # The two sets of cars are infinitely far away from each other at the beginning.
    distance_between_cars = float('inf')

    while i < n and j < n:
        # Calculate the distance between current cars in the two sets.
        distance = abs(cars1[i].speed - cars2[j].speed)

        # If the distance is less than the remaining distance to the next car in either set, predict a collision.
        if distance < distance_between_cars:
            collision_count += 1
            distance_between_cars = 0
            # Since the cars are infinitely sturdy and strong, we simply move forward by the distance between the cars without stopping.
        else:
            distance_between_cars -= distance
        # Move the left and right pointers forward
        i += 1
        j += 1

    # Return the number of collisions
    return collision_count