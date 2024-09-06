def car_race_collision(n):
    # Define 2 lists to hold the cars from each direction
    cars_left_to_right = list(range(n))
    cars_right_to_left = list(range(n))

    # Define 2 counters to keep track of collisions
    collisions_left_to_right = 0
    collisions_right_to_left = 0

    # Move each car in both directions in infinite time
    for i in range(n):
        # Move car i from left to right
        if cars_right_to_left[i] == cars_left_to_right[i]:
            collisions_left_to_right += 1
        else:
            cars_left_to_right.remove(cars_left_to_right[i])
            cars_left_to_right.append(cars_right_to_left[i])

        # Move car i from right to left
        if cars_left_to_right[i] == cars_right_to_left[i]:
            collisions_right_to_left += 1
        else:
            cars_right_to_left.remove(cars_right_to_left[i])
            cars_right_to_left.append(cars_left_to_right[i])

    return collisions_left_to_right, collisions_right_to_left