```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Each car moves in the same speed. Two cars
    after driving towards each other will collide when 
    a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, so they continue moving in their 
    trajectory as if they did not collide. This function outputs the. the number of collisions between 
    these cars.
``` 
This script defines a function `car_race_collision` that simulates a race collision between n cars on a straight road. It follows the rules of the cars moving toward each other, and colliding when the front of one car meets the back of the other.