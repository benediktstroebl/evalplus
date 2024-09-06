```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As the two sets of cars start out being very far from each other. All cars move in the same speed.
    The cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.
    The function outputs the number of collisions.
```
def test_collision():
    assert car_race_collision(4) == 3  # 4 cars, driving left and right, should collide exactly 3 times.
The function `car_race_collision` calculates the number of collisions in a race between cars driving left and right on a straight road. The test function `test_collision` verifies the output of the `car_race_collision` function for the given input `n = 4`.