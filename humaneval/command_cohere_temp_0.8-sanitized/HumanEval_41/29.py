def car_race_collision(n):
    # initialize two lists to hold the positions of the cars
    car_1 = [i for i in range(n)]
    car_2 = [i for i in range(n)]
    
    # assume the cars start at different points, far from each other
    car_1[0] += 1e9; car_2[0] += 1e9
    
    # iterate through the cars, moving them incrementally closer to each other
    for _ in range(2 * n):
        car_1[(car_1[0] // 2) % n] += 1; 
        car_2[(car_2[0] // 2) % n] -= 1
        
        # check for collisions by comparing car_1 and car_2 lists element-wise
        collisions = sum(1 for i, j in zip(car_1, car_2) if i == j)
        if collisions > 0: return collisions
    
    return 0