```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Each car keeps moving in its same speed. 
    Two cars will collision. 
    The Car 1 hits Car 2, then Car 2 continues moving, as if it did not collide.
    Car 2 collides with Car 3, then Car 3 continues moving, as if it did not collide.
    ...
    This remaining cars, each car keeps moving in its original trajectory.
    return the number of collisions.
```
This Python code defines a function called `car_race_collision` that simulates a car race collision scenario. It takes the `n` parameter `n` that represents the number of cars participating in the race. 

The `car_race_collision` function follows a sequential collision logic. It simulates a collision between pairs of cars, with each collision causing the subsequent car to continue moving as if it did not collide. 

The function then returns the number of collisions that occurred during the race.