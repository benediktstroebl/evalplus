def car_race_collision(n):
    # Calculate the number of collisions for one set of cars (n)
    collisions = n // 2  # Divide by 2 since the cars are equally likely to collide with the front or the back car
    
    # When there are n cars, there are 2n total cars on the road (2 sets of n cars each)
    total_cars = 2 * n
    
    # Return the number of collisions when 2n cars are on the road
    return collisions / total_cars