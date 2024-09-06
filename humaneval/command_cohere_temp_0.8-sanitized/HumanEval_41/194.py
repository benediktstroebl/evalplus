def car_race_collision(n: int):
    # Define the two lists to store car positions for each team
    l1, l2 = [], []
    
    # Define the car positions for each team at different time steps
    for i in range(n):
        l1.append(i)
        l2.append(n - i - 1)
    
    # Find the collisions in the first n cars
    collisions = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if l1[i] > l2[j] and l1[i] < l2[j] + n:
                collisions += 1
                break
    return collisions