```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    Two cars want to collide.
    When the each set of cars start out being very far from each other. All cars move in the same speed.
    All cars continue moving in their direction as if they did not collide.
    Returns: number of collisions (0 based on the cars not colliding).
    """

    # Set n equal to the number of cars in the race
    n = int(input("Enter the number of cars: "))

    # Initialize a count of collisions
    collisions = 0

    # Check for collisions one by one
    for i in range(n):
        direction = input("Enter direction (left/right): "). right")
        if direction == "right":
            x = float(input("Enter x value for right: "))
            y = float(input("Enter y value for right: "))
            # Calculate the position of the left car
            left_position = [x, y]
        elif direction == "left":
            x = float(input("Enter x value for left: "))
            y = float(input("Enter y value for left: "))
            # Calculate the position of the right car
            right_position = [x, y]
        else:
            print("Invalid direction. Please enter 'left' or regular (left' or 'right').")
            return

        # Compare the positions of the cars
        if left_position < right_position:
            # The left car is driving left, so it should be in front of the right car
            collision = [left_position, right_position]
        else:
            # The right car is driving left, so it should be in the back of the left car
            collision = [right_position, left_position]

        # Increment the count of collisions
        collisions += 1

    return collisions
```
This Python script defines a function called `car_race_collision` that simulates a car race collision. It takes the by asking the user to input the number of cars in the race and then uses a loop to check for collisions between each pair of cars. 

The script calculates the relative position of each car and uses this information to determine when a collision occurs.