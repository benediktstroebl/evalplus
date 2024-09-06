def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move towards each other on an infinitely long straight road.

    Parameters:
        n (int): Number of cars in each set.

    Returns:
        int: Number of collisions between the moving cars.
    """

    # Define the two sets of cars as two lists where each index represents the ith car's position.
    car1 = [i for i in range(n)]
    car2 = [i for i in range(n, 0, -1)]

    # Initialize collisions as 0, it increments when car1[i] intersects with car2[i].
    collisions = 0

    # Iterate through each car in the first set.
    for i in range(n):
        # Find the car from the second set that intersects with the current car from the first set.
        k = car2.index(min(car2, key=lambda x: abs(car1[i] - x))) + 1
        # If the difference between the cars' positions is less than or equal to 1, a collision occurs.
        if abs(car1[i] - car2[k-1]) <= 1:
            collisions += 1
        # Remove the intersecting car from the second set, as we don't need to check it again.
        del car2[k-1]

    # Return the total collisions.
    return collisions