Here's a self-contained Python function that solves the car race collision problem for any number of n cars, returning the number of collisions:
```python
def car_race_collision(n: int):
    # Define the starting positions of each car
    car_positions = [-i for i in range(n)]
    # Define the speed of each car (positive represents rightward motion)
    speeds = [1] * n
    # Define the time interval
    time = 0
    # Set the time interval to 0 to start computation
    for _ in range(n):
        # Move all cars for this iteration
        for i in range(n):
            car_positions[i] += speeds[i] * time
        # Calculate the next time interval
        time += 0.01  # The precise calculation is important for precise results
        # Find the index of the first car that hits the left-right boundary
        collision_index = [i for i, j in enumerate(car_positions) if j == 0 or j == n].index(car_positions[i] < 0)
        # Return the number of collisions
        return len(collision_index)
```
This function works by defining the starting positions and speeds of each car, and then iteratively moving each car according to its speed. It uses a the to calculate the next time interval, and then finds the index of the first car that hits the left-right boundary. The number of collisions is then returned as the final output.