```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed.

    A car moving left to right collides with another car that's moving right to left. As they are infinitely strong, they continue moving in their trajectory as if they did not collide. The number of collisions is returned.

    :
    function tests using a following test:
    Test case 1: n = 4
    assert car_race_collision(n) == 2
    Test case 2: n = 5
    assert car_race_collision(n) == 2
    Test case 3: n = 6
    assert car_race_collision(n) == 0
    ```

The function `car_race_collision` takes an integer `n` as input, which represents the number of cars on the road. The function simulates the cars moving towards each other on the road, and the number of collisions is returned.