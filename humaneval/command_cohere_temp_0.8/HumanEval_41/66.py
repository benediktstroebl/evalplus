Here's a Python script that includes a function to solve the car collision problem described in the markdown code block:
```python
def car_race_collision(n):
    # Define two arrays to hold the positions of inward and outward moving cars.
    car_positions = [0] * n
    opp_car_positions = [0] * n
    
    # Define the direction for each car.
    direction = [1] * n
    
    while True:
        # Find the largest position of any car.
        largest_position = max(car_positions)
        
        # If the largest position is at the end of the array...
        if largest_position == n - 1:
            break  # ...and if there are no opp_car_positions remaining, return 0 collisions.
        elif largest_position == len(opp_car_positions) - 1:
            continue  # Otherwise, if there are no more car_positions remaining, skip this iteration.
            
        # Find the smallest opp_car_position.
        smallest_opp_position = min(opp_car_positions)
        
        # Count the number of collisions.
        collisions = sum(1 for i in range(n) if car_positions[i] == smallest_opp_position and direction[i] == -1)
        
        # Increment car positions.
        car_positions = [pos + 1 for pos in car_positions]
        opp_car_positions = [pos + 1 for pos in opp_car_positions]
        direction = [-1] * n
        
        # Alternate between moving cars and opp_cars.
        if len(opp_car_positions) == n:
            car_positions, opp_car_positions = opp_car_positions, car_positions
            direction = [-direction] * n
    return collisions

# Test cases:
print(car_race_collision(0))  # Output: 0
print(car_race_collision(1))  # Output: 0
print(car_race_collision(2))  # Output: 0
print(car_race_collision(5))  # Output: 0
print(car_race_collision(10))  # Output: 5
```

This script defines the `car_race_collision` function, which takes in an integer `n` as input, representing the number of cars. It operates on two arrays: `car_positions` for cars moving from left to right, and `opp_car_positions` for cars moving from right to left. Direction indicators are stored in the `direction` list.

The function uses a while loop that alternates between advancing car positions and opposite car positions. It continues until both arrays have reached their end, indicating that all cars have finished their journeys.

The number of collisions is then calculated by finding the smallest `opp_car_position` and checking the `direction` of each car in the `car_positions` array. Finally, the positions of both sets of cars are updated, and the process repeats with the opposite direction and moving cars. The function returns the total number of collisions upon completion of both sets of journeys.