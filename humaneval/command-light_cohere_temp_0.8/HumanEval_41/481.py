```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. Each car has the Friction with other to have collision, they continue moving
    in their trajectory as if they did not collide. 

    cars are infinitely sturdy and strong.

    # Calculate the time until the first car driving right to collision 
    time = 0
    for i in range(n):
        # Move car right
        time += i * 1
        # Check if first car hits the wall (ie, the right-moving car) 
        if time >= n * 1:
            return time  # Return time as the number of collisions

    # Return time
    return -1  # Return -1 if no collision occurs

# Test the function
for i in range(10):
    time = car_race_collision(i)
    if time != -1:
        print(f"Collisions happen at {time}")
```

This code creates a function that simulates car accidents on a straight road. The cars move at a same speed, and if they meet, they collide and continue moving in the same direction. The function returns the time if a collision occurs, and -1 if no collision happens.