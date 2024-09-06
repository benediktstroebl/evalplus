def car_race_collision(n: int):
    # Define the two groups of cars
    car_1 = [i for i in range(n)]
    car_2 = [i for i in range(n)]
    
    # Define the collision boolean list
    collision = [False] * (2 * n)
    
    # Iterate over both lists of cars to detect collisions
    for i in range(n):
        if car_1[i] == car_2[-(i + 1) % n]:
            collision[i] = True
    
    # Return the number of collisions
    return sum(collision)