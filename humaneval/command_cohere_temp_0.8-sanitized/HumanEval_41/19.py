def car_race_collision(n: int):
    # Initialize two lists to hold the positions of left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n)]

    # Initialize collision variable to zero.
    collisions = 0

    # Iterate through each pair of cars.
    for i in range(n - 1):
        # If the cars are on the same position, increment the collision variable.
        if left_driving[i] == right_driving[i]:
            collisions += 1
        # Move the right driving car to the right.
        right_driving[i + 1] = right_driving[i] + 1

    # Move the left driving cars to the right.
    for i in range(n - 1):
        left_driving[i + 1] = left_driving[i] + 1

    # Reverse the right_driving list and return the number of collisions.
    return collisions + sum([1 if left_driving[i] == right_driving[i] else 0 for i in range(n)])