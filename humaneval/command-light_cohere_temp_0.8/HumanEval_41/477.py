```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. Each car will collide and keep moving as if they did not. 
    The number of cars driving left to right is n, and the number of cars driving right to left is n. 
    The two cars are moving in opposite directions, and they collide with each other when they meet. 
    The function outputs the number of collisions, which is the number of cars that collided.
    """return sum(1 for i in range(n))
```
The output of this code will be the total count of the cars that collided, as predicted.