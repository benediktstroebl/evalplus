def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [0] * n
    right_cars = [0] * n

    # Define the number of possible collisions, initially 0
    total_collisions = 0

    # Calculate the number of collisions when n is odd
    if n % 2:
        left_cars[0] = 1
        right_cars[0] = 1
        total_collisions += 1

        for i in range(1, n):
            if left_cars[i] == right_cars[i]:
                total_collisions += 1
            left_cars[i] += 1
            right_cars[i] += 1

    # Calculate the number of collisions when n is even
    else:
        for i in range(1, n - 1):
            if left_cars[i] == right_cars[i]:
                total_collisions += 1
            left_cars[i] += 1
            right_cars[i] += 1

        # Handle the case where both ends of the even number of cars collide
        left_cars[n - 1] = 1
        right_cars[0] = 1
        total_collisions += 1

    # Return the total number of collisions
    return total_collisions