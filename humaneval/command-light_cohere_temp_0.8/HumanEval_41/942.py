Here's the Python script with the self-contained function:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars move in the same speed, and two cars want to collide.
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    return:
    if len(set([tuple(i, j) for i in range(n) for j in range(n)])) == 2:
        return True
    return False
```
This script defines a function car_race_collision that checks whether two cars at opposite ends of the road will collide. It uses a specific logic for identifying collisions in a "race collision" scenario, where cars are moving towards each other along a straight line.