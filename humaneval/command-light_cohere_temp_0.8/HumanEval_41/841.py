```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    These two function is to collide.
    Each car has a same constant speed. Two cars, driving towards each other, will collide
    when one hits the other car.
    The two cars are infinitely sturdy and strong, so they will continue moving
    in their direction as if they did not collide.
    The function outputs the number of collisions.
```
This function takes in a single integer, n, which is the number of cars on the road. It works by simulating the cars driving towards each other on a straight line, and counting the number of collisions between them. The function then returns the number of collisions, which is the number of cars that were moving towards each other and collided.