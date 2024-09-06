Here is a self-contained Python script that solves the problem of cars on a race track colliding:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed. A car that's moving left to right hits a car that's moving right to left. The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    The function outputs whether a collision happened.
    """
    number of collisions is 1
    n-2 car - car collisions happen when two cars meet. In the first scenario, the cars are driving on the same straight line, so they would collide. In the second scenario, the cars are driving on opposite directions, so they would miss each other and continue moving.

In this solution, we use a simple heuristic that checks if the absolute difference between the positions of the two cars is less than a threshold. This heuristic is a car that's moving left to right hits a car that's moving right to left, and they would collide if they were on the same straight line. 

This solution is self-contained and does not require any additional data or functions.