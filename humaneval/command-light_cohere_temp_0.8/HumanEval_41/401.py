```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and continue moving in their trajectory as if they did not collide.

    return number of collisions
   
    """
    Test cases:
    assert car_race_collision(2) == 2
    assert car_race_collision(3) == 3
    assert car_race_collision(4) == 4
    assert car_race_collision(100) == 100

    real_world cars on the track!
    ```

The function `car_race_collision` calculates the number of collisions when n cars are driving on a straight road towards the opposite direction simultaneously. The test cases ensure that the function provides the correct output.