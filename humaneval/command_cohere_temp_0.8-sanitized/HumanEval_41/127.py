def car_race_collision(n):
    # Initialize two lists to represent the position of each car.
    car_1 = [i for i in range(n)]
    car_2 = [i for i in range(n)]
    
    # Define the direction of each car. Default is right-to-left.
    dir1 = [-1] * n
    dir2 = [1] * n
    
    # Iterate until a collision occurs or until both lists are sorted.
    while car_1 != car_2 or dir1 != [-1] * n or dir2 != [1] * n:
        for i in range(n):
            if car_1[i] > car_2[i]:
                # Switch the direction of the car that's moving right-to-left.
                dir2[i] = -1
            elif car_1[i] < car_2[i]:
                # Switch the direction of the car that's moving left-to-right.
                dir1[i] = 1
            else:
                continue
        
        # Sort both lists based on the current direction.
        car_1.sort(key=lambda x: dir1[x])
        car_2.sort(key=lambda x: dir2[x])
    
    # Return the number of collisions. This occurs when a car switches direction.
    return sum(dir1 != [-1] * n and dir2 != [1] * n)