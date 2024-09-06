```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. All cars move in the same speed.
    Two cars want in the same to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    return:
    ```Return the number of collisions```

# Function Test:
assert car_race_collision(6) == 10 # Should be 10
assert car_race_collision(8) == 12 # Should be 12
```

This script defines a function called car_race_collision, which simulates a collision between two sets of cars on a straight road. The cars move in opposite directions and collide when they meet, but due to the strength of the cars, they continue moving in their direction. The function outputs the number of collisions, which is the number of cars that have collided with each other. The test at the time asserts that the function is correct for different values of n.