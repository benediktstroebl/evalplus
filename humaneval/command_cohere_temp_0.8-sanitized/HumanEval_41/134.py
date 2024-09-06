def car_race_collision(n):
    # Initialize two lists to represent the positions of cars
    left = [i for i in range(n)]
    right = [i for i in range(n)]
    
    # Initialize collision counter
    collisions = 0
    
    # Iterate through each car on the left moving towards the right
    for i in range(n):
        while len(left) and left[0] <= right[len(right) - 1]:
            # If the car on the left is in front or at the same position as a car on the right, increment collision counter
            collisions += 1
            left.pop(0)
            right.pop()
    
    return collisions