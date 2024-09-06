def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n)]

    # Initialize collisions counter
    collisions = 0

    # Iterate until cars of the 2 lists intersect
    while len(left_driving) > 0 and len(right_driving) > 0 and left_driving[0] != right_driving[0]:
        if left_driving[0] < right_driving[0]:
            left_driving.pop(0)
        else:
            right_driving.pop(0)

        # If the first car in one list has a corresponding car in the other list, increment collisions
        if left_driving[0] == right_driving[0]:
            collisions += 1

    return collisions