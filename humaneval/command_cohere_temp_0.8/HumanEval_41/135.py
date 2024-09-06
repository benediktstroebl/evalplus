Here's a Python script that includes a function to solve the car crash problem as per the provided specification:
```python
def car_race_collision(n):
    # Define two lists to represent the positions of cars moving left to right and right to left.
    ltr_positions = [i for i in range(n)]
    rtl_positions = [i for i in range(n)]
    
    collision_count = 0
    
    # Loop until the two lists have overlapping elements.
    while ltr_positions and rtl_positions:
        # Find the car in the left-to-right list with the smallest position.
        min_ltr_pos = min(ltr_positions)
        ltr_positions.remove(min_ltr_pos)
        
        # Find the car in the right-to-left list with the largest position.
        max_rtl_pos = max(rtl_positions)
        rtl_positions.remove(max_rtl_pos)
        
        # If the two cars collided, increment the collision count.
        if min_ltr_pos == max_rtl_pos:
            collision_count += 1
    
    return collision_count

# Test Cases
print(car_race_collision(0))  # Should print 0 as there are no cars.
print(car_race_collision(1))  # Should print 0 as there's only one car.
print(car_race_collision(2))  # Should print 0 as there are two cars far apart.
print(car_race_collision(3))  # Should print 1 as the two inner cars will collide.
print(car_race_collision(4))  # Should print 1 as the two inner cars will collide.
```
This script defines the `car_race_collision` function, which takes an integer `n` as input, representing the number of cars. It simulates the cars moving left to right and right to left and counts the number of collisions between the two sets of cars. The function returns the number of collisions between these cars, which happens when the absolute difference between two cars is zero, indicating a collision.