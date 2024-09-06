```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. Each car keeps moving at the same speed. 
    When two cars are moving at the same speed to collide
    when a car that's moving left to right hits a car that's moving right to left. 
    The function outputs number of collisions.
    """. The cars are infinitely sturdy and strong, as a result, they continue moving
    in their trajectory as if they did not collide.
    """
return sum(1 for i in range(n))
```
This function is designed to simulate a car race collision scenario. It takes the input of a number of cars 'n' and returns the total number of collisions.

The function uses a simple looping formula to simulate the cars moving towards each other and colliding. The collisions are then the sum of 1 for each pair of cars, which results in the total number of collisions.

This function is self-contained and provides a solution to the problem of counting the number of collisions in a car race.