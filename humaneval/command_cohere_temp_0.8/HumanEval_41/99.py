Here's a Python script that includes a function to solve the car crash problem as per the provided instructions:
```python
def car_race_collision(n: int):
    # Define two lists to store car positions for each group
    cars_left_to_right = [i for i in range(n)]
    cars_right_to_left = [i for i in range(n)]

    # Define a variable to track collisions
    collisions = 0

    # Iterate through each car in the left-to-right group
    for i in range(n):
        # Check if any cars in the right-to-left group is at the same position or greater
        if cars_right_to_left[i] == i or cars_right_to_left[i] >= i + 1:
            collisions += 1

        # Increment the position of the car in the left-to-right group
        cars_left_to_right[i] += 1

    # Iterate through each car in the right-to-left group
    for i in range(n):
        # Check if any cars in the left-to-right group is at the same position or greater
        if cars_left_to_right[i] == i or cars_left_to_right[i] >= i + 1:
            collisions += 1

        # Increment the position of the car in the right-to-left group
        cars_right_to_left[i] += 1

    return collisions
```

This script defines the `car_race_collision` function, which takes an integer `n` corresponding to the number of cars as input. The function takes advantage of the fact that the cars are infinitely strong to terminate collisions. By doing so, the cars effectively move each other out of the way, and this results in a cleaner movement of cars without collisions. The output of this function is the number of collisions that take place during the race. 

The function outputs the number of collisions between cars driving left to right and cars driving right to left, as described in the problem statement. You can also verify the correctness of the function by testing it against specific values of `n`.