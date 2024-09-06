def car_race_collision(n: int):
    cars_left = []
    cars_right = []
    for i in range(n):
        x_left = i / (n - 1)
        cars_left.append(x_left)
        
        x_right = (n - i - 1) / (n - 1)
        cars_right.append(x_right)
    
    collisions = len(set(cars_left).intersection(cars_right))
    
    return collisions