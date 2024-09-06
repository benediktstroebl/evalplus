```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    This cars are in the same speed and infinitely strong, as a result, they continue moving in their trajectory as if they did not collide.
    This function outputs the value of total collisions.
    return the total_collisions

def test_collision(n: int):
    return n == car_race_collision(n).approx that the number of collisions matches the expected value
```

This script defines a function car_race_collision that simulates a collision between n cars on a straight road. The test_collision function checks if the number of collisions is equal to the expected value based on the input n.