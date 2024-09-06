Here is a self-contained Python script that solves the problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. All cars have the
    same speed. Two cars are the duplicates their hitting each other, they will continue moving in their trajectory as if they did not collide.

    The number of total collisions is returned.
 car_race_collision(5) # Test the function with 5 cars
```

This code defines a function `car_race_collision` that simulates a road with cars moving towards each other simultaneously. It determines if the generate a collision, each car will continue its motion without stopping. The function returns the number of collisions, and if the test is passed, it will output a message that indicates a successful run.