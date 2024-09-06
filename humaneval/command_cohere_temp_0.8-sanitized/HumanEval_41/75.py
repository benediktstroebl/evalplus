def car_race_collision(n: int):
    # Define 2 lists to store the positions of inward and outward moving cars.
    left_to_right = [0] * n
    right_to_left = [0] * n

    # Calculate the collision points
    for i in range(n):
        # Find the ith car moving left to right where i is the index of the list.
        left_to_right_car = i
        # Find the first available - infinity or a car moving right to left.
        right_to_left_car = right_to_left.index(0) if right_to_left[0] == 0 else right_to_left.index(-1)
        
        # If a car exists, increment the collision count and reset the right_to_left list.
        if left_to_right_car <= right_to_left_car:
            right_to_left[right_to_left_car] = i + 1
        else:
            right_to_left[i] = i + 1

        # Shift the relevant indexes of the right_to_left list to remove the caught car.
        right_to_left = right_to_left[:right_to_left_car] \
                        + [right_to_left_car + 1] \
                        + right_to_left[right_to_left_car + 1:]

    return sum(left_to_right) - sum(right_to_left)