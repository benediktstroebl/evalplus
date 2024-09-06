def car_race_collision(n):
    # Initialize two lists to hold the positions of the cars
    car_1 = [i for i in range(n)]
    car_2 = [i for i in range(n)]
    
    # Define the number of collisions based on the number of cars
    collisions = n - 1
    
    # Move each car in the first list to the right by one position
    for i in range(1, n):
        car_1[i] = car_1[i-1] + 1
    
    # Move each car in the second list to the left by one position
    for i in range(n-2, -1, -1):
        car_2[i] = car_2[i+1] - 1
    
    # Compare the two lists to find collisions
    for i in range(n):
        if car_1[i] == car_2[i]:
            collisions -= 1
    
    return collisions