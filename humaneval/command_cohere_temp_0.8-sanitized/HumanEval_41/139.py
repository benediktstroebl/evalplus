def car_race_collision(n):
    # Define two lists to represent the position of each car.
    car_left = [i for i in range(n)]
    car_right = [i for i in range(n, 2 * n)]

    # Define the collisions as a boolean list to initially be False.
    collisions = [False for i in range(n)]

    # Slide the right-going cars right by one, and slide the left-going cars to the right
    # Then, compare if the ith car in car_left is equal to the ith+n car in car_right, if so, set collision[i] to True.
    for i in range(n):
        car_left[i] += 1
        car_right[i] -= 1
        if car_left[i] == car_right[i]:
            collisions[i] = True

    # Return the number of collisions.
    return sum(collisions)