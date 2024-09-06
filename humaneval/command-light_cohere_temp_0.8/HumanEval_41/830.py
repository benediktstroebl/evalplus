```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars have the particular speed. Two cars that are moving towards each other collide, and they continue moving in their trajectories as if they did not collide. The cars are infinitely sturdy and strong.

return:
    number_of_collisions = n * (n - 1) // 2
    return number_of_collisions

# Test the function
assert car_race_collision(3) == 6

# Test with large input
assert car_race_collision(1000) == 500010

```

This Python script defines a function called car_race_collision that simulates a car race collision scenario. It takes a number of cars on the road, where some are driving left and others are driving right. The cars are assumed to be infinitely strong and will continue moving along their trajectories even after colliding. The function calculates the number of collisions by multiplying the number of cars by the difference between their quantities. The function then returns the number of collisions. The test cases are used to verify if the function works correctly.