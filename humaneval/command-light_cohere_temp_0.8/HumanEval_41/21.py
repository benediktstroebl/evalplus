Here's the Python script that you requested:

```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed; two cars move in opposite directions collide. The cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.
    The function outputs the collisions number
    """

    return sum((-i for i in range(n)) if i in [n//2, n//2+1, n//2+n]))
```

This script defines a function `car_race_collision` that simulates a car race collision scenario. It takes the number of collisions by checking if the car is driving left towards the center of the lane or moving towards the observer's right. The function uses a summation of the indexes of the two cars that are moving in opposite directions and colliding with each other.