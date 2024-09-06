def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2 * n)]

    # Find indexes of cars that will collide
    collide_left = [j for j in range(n) if left_cars[j] == right_cars[j]]
    collide_right = [j for j in range(n) if right_cars[j] == left_cars[n + j]]

    # Combine the indexes of colliding cars and remove duplicates
    collisions = list(set(collide_left + collide_right))

    return len(collisions)