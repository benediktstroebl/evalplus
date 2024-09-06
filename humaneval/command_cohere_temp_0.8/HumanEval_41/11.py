Here's a Python script that includes a function to solve the car crash problem as per the provided specification:
```python
def car_race_collision(n: int):
    # Initialize two lists to hold the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Find the collision points
    for i in range(n - 1): 
        # If a left car finds a right car, remove it from both lists
        if left_cars[i] == right_cars[i]: 
            del left_cars[i]
            del right_cars[i]
        # If a right car finds a left car, remove the latter since it's considered hit
        elif left_cars[i] > right_cars[i]:
            del left_cars[i]
    # Count the number of left moving cars
    return len(left_cars)
```
This function uses two lists to keep track of the positions of the left-moving and right-moving cars. It then iterates through each possible pair of cars and removes them from the lists if they match, considering it a collision. Finally, it counts the number of remaining left-moving cars to determine the number of collisions.