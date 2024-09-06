Here is a self-contained Python script that defines and solves the car race collision problem in a markdown code block:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    The two cars are infinitely sturdy and strong, so they continue moving
    in their trajectory as if they did not collide.

    # Collision Detection Loop
    The first car is moving left and the second car is moving right.
    if n == 1:
        return 0  # No collision yet
    elif n == 1:
        return 1  # Collision detected: First car hits second car
    elif n == 2:
        return 1  # Collision detected: First car hits second car
    else:
        return 0  # Collision detected: Too many cars to have collision
```

This script provides a function called **car_race_collision**, which simulates the collision of two cars on a straight road. The function takes in the number of cars **n** as input and returns the number of collisions detected.