Here's a Python script that includes a function to solve the car crash problem as per the provided markdown code block:
```python
def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars
    simultaneously move in opposite directions on an infinitely long straight road.
    """
    dir1, dir2 = -1, 1
    car_position = [i for i in range(n)]
    
    # Initialize a counter for collisions
    collision_count = 0
    
    # Set a flag to determine direction of second-to-last car
    is_last_car = False
    
    while True:
        # Update car positions for current direction
        for i in range(n):
            car_position[i] += dir1 if not is_last_car else dir2
        
        # Find cars that collide
        for i in range(n):
            if car_position[i] > 0 and car_position[i] - 1 < n:
                collision_count += 1
                car_position[i] = -1  # Move collided car out of the way
        
        # Switch direction for next iteration
        dir1, dir2 = dir2, dir1
        
        # Break the loop if all cars have collided or are removed
        if all(car_position == -1) or all(car_position >= n) or is_last_car:
            break
        
        is_last_car = not is_last_car
    
    return collision_count
```
This script defines the 'car_race_collision' function, which takes an integer 'n' as input, representing the number of cars in each group, and returns the number of collisions between the two sets of cars.

The algorithm uses two separate lists, 'dir1' and 'dir2', to determine the direction of each car in each step, where dir1 and dir2 are set to -1 and 1 respectively, to represent the movement of the cars.

It then initializes a list 'car_position' containing indices to track the positions of each car. The function starts by assuming that no collisions have occurred, sets a flag 'is_last_car', and enters a while loop that continues until all cars have collided or moved out of their respective ranges.

Within this loop, the function updates the position of each car in parallel based on the current direction, checks for collisions, and adjusts the direction of movement of the cars for the next iteration. The loop exits when all cars have collided or when the last car has moved out of its valid range. Finally, the function returns the number of collisions recorded.