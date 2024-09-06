Here's a Python script that includes a function `car_race_collision(n)` which solves the problem you described:
```python
def car_race_collision(n):
    # Initialize two lists to hold the positions of left-moving and right-moving cars
    moving_left = [0] * n
    moving_right = [0] * n

    # Define a variable to track the number of collisions
    collisions = 0

    # Iterate through each car in the collision
    for car in range(n):
        # Move the right-moving cars to the right and the left-moving cars to the left
        moving_right[car] += 1
        moving_left[n - 1 - car] += 1

        # Check for collisions
        if moving_right[car] > moving_left[n - 1 - car]:
            collisions += 1

        # Reset the position of the left-moving and right-moving cars for the next iteration
        moving_right[car] = 0
        moving_left[n - 1 - car] = 0

    return collisions
```

This script defines the `car_race_collision` function, which takes in an integer `n` as its argument and returns the number of collisions between the two sets of cars moving in opposite directions. 

The algorithm works by tracking the position of each car. Cars moving from left to right are represented by a positive position in the `moving_left` list, while cars moving from right to left are represented by a positive position in the `moving_right` list. 

At each step of the simulation, both sets of cars move one position. The algorithm then checks for collisions by comparing the positions of cars in opposite directions. If a car moving from left to right has a greater position than a car moving from right to left, a collision occurs. 

To keep track of the number of collisions, the algorithm uses the `collisions` variable, which is incremented each time a collision is detected. Finally, to reset the position of the cars for the next iteration, the algorithm sets the position of both sets of cars back to 0. 

This algorithm is designed to simulate the described car race scenario and provide the number of collisions between opposite-direction cars within a single function, without the need for external modules or dependencies. 

You can use this code to solve the given problem and determine the number of collisions between the two sets of cars moving in opposite directions.  If you have any questions about the solution, please let me know!