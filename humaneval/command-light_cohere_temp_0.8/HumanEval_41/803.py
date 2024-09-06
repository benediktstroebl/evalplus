```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars will moving to collide when a car that's moving left to right hits a car that's moving right to left. The cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.
    Returns the number of collisions.

```

def test_collision(n: int):
    # Test cases
    assert car_race_collision(10) == 10
    assert car_race_collision(20) == 0
    assert car_race_collision(0) == 0
    assert car_race_collision(5) == 5
    assert car_race_collision(15) == 0

```
This Python script defines a function `car_race_collision` that simulates a collision of cars on a straight road. The function takes an input `n` representing the number of cars on the road, and returns the number of collisions that occur. 

The function is then tested using the `test_collision` function, which provides a series of input values and asserts that the output of `car_race_collision` is correct for each input.