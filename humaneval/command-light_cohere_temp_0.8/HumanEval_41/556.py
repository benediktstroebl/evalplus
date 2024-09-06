```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars have in the same speed; two cars meet in the middle and collide. 

    function outputs the UNIQUE number of collisions.

return count = sum(c>0 for c, car in zip(c1, c2) if car[0] == car[1] and c1[0] < c1[1]))
``` 
This Python function car_race_collision simulates a road with two streams of cars moving in opposite directions. It then calculates the unique number of collisions by considering the order of cars in the collision. The cars are infinitely strong, so they continue moving in their original direction. The function returns a number of collisions that occur in the scenario.