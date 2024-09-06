def car_race_collision(n: int):
    # Initialize two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Sort the lists according to their positions. Cars at the same position will collide.
    l2r.sort()
    r2l.sort()
    
    # Initialize a variable to count the number of collisions.
    count = 0
    
    # Iterate through the two lists. If a car in the left to right list matches with a car in the right to left list, increment the collision count.
    for i in range(n):
        if l2r[i] == r2l[i]:
            count += 1
    
    return count