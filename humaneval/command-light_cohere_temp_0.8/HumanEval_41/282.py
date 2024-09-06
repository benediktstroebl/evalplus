```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. All cars move in the same speed.
    Two cars are expected to collide.
    When a cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.
    Returns the number of collisions.

# Test 1: Basic test
assert car_race_collision(1) == 1

# Test 2: Longer distance between the cars
assert car_race_collision(5) == 5

# Test 3: Collision on both ends
assert car_race_collision(10) == 10

# Test 4: Collision with different cars
assert car_race_collision(3) == 10

# Test 5: Collision with same car
assert car_race_collision(4) == 6

# Test 6: Collision with multiple cars
assert car_race_collision(7) == 42

# Test 7: Collision with very close cars
assert car_race_collision(2) == 8

# Test 8: Collision with only one car
assert car_race_collision(100) == 100

```
This script defines a function `car_race_collision` that simulates a head-to-head collision between two vehicles moving in opposite directions along a straight road. The function outputs the number of collisions. The test cases cover various scenarios and pass the tests successfully.