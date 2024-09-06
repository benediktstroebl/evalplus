```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. Each car is moving on its own speed and is infinitely sturdy. 
    Two cars are each to collide. When a car that's moving left to right hits a car that's moving right to left, the two cars will continue moving
    in their trajectory.

    The function outputs the collision number.
    """
return 2 **n*(n-1)/2
```

The function `car_race_collision` takes an integer `n` as input, which represents the number of cars on the road. The function uses mathematical logic to determine when and how the cars collide with each other. The function returns the number of collisions, which is the product of all possible pairs of cars that collide.