Here is a Python script that contains a self-contained function that solves the Car Race Collision Problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are moving right to right; simultaneously, a different set of n cars are driving right to left. 
    All cars have the all in the same speed
    and are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.
    The function outputs the collision number
    """
    Let's say there are n sets of cars. 
    For each car that's moving left to right, when it hits a car that's moving right to left, it will continue moving in its trajectory.
    we'll call the for the most sets of cars in the road, and for each car, we calculate the minimum time it takes to reach the other car. We will then the this time, we'll have a list of the minimum time for each car to collide.

We'll also need to calculate the time it takes to reach the other car when it's moving right to left. The time will be the same for each car because they're moving at the same speed.

So, for each car, we calculate the time it takes to reach the other car, and if this time is greater than the minimum time, we'll have a collision. 

We'll return True if there are no collisions, otherwise, the number of collisions.