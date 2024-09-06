Here's the solution to the car race collision problem using a self-contained Python function:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    # Two cars will to collide
    when a car that's moving left to right hits a car that's moving right to left, the two cars will
    continue moving in their original direction of motion.

    # Define the fact that is the two cars have collided.
    # Then no collision, return False
    elif (abs(n[0] - n[1]) <= 1):
        return True
    else:
        return False
```

This function takes an integer n as input and returns a boolean value indicating whether two cars with IDs n[0] and n[1] collided on the road.

It uses a basic approach to check if the absolute difference between the two car IDs is less than or equal to 1. The cars will collide if the difference is smaller.