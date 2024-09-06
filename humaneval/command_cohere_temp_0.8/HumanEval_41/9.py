Here's a Python script that includes a function to solve the car crash problem as per the provided markdown code block:
```python
def car_race_collision(n: int):
    # Initialize two lists to keep track of cars moving left to right and right to left
    moving_right = [False] * n
    moving_left = [False] * n
    
    # Toggle the movement of every second car
    for i in range(1, n, 2):
        moving_right[i] = True
    
    for i in range(0, n - 1, 2):
        moving_left[i] = True
    
    # Count the number of collisions
    collisions = sum(1 for i in range(n) if moving_right[i] and moving_left[i])
    
    return collisions
```
This function operates on the premise that there are 2n cars in total, alternating between moving left-to-right and right-to-left. It initializes two lists to track the movement of these cars, alternating their movement in subsequent steps. Finally, it calculates the number of collisions by evaluating whether movement conflicts occur for each car using a generator expression.