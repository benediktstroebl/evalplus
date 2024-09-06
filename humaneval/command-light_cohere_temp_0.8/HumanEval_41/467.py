```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    All cars move in the same speed;  two cars will collide
    as they reach each other on the road. The cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    return:
    ``` Return the number of collisions between all cars.
    Return a
    number of collisions is the number of pairs of cars that collide.
    Check:
    print(collisions == n // 2)
``` 
This script defines a function `car_race_collision` that simulates a collision of `n` cars on a straight road. The cars drive towards the scenario where two cars will collide if they are driving towards each other and will continue moving in their original direction as if they had not hit. The `collisions` variable keeps track of the number of collisions, which is equal to `n // 2` because each car pair will collide twice.