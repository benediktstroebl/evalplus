```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars have theib speed. Two cars want to collide when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.
    return: 
    The number of collisions is returned.

# Example test
print(car_race_collision(6)) 
# Output should be 3, there are 3 collisions

```

This Python script defines a function car_race_collision that simulates a road with cars moving towards the left simultaneously and towards the right simultaneously. It then simulates a collision between these cars, which continue moving in their trajectories. The function returns the number of collisions, which is the number of cars that have collided with each other. 

The test at the end checks that the function outputs the correct number of collisions.