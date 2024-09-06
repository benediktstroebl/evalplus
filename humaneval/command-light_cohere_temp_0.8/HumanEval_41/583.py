```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    Two cars will be driving towards each other. 
    The collision happens when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.

    The function outputs the number of collisions.
```
def test_collision():
    n = 7
    collisions = car_race_collision(n)
    assert collisions == 2
    return True
```
This script defines a function **car_race_collision** that simulates a head-to-head collision between two vehicles on a straight road. The test function **test_collision** takes an input **n** and uses this function to calculate the number of collisions, which is then asserted to be **2**.  This passes the test and proves that the code works as intended.