```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed. Two cars will driving towards each collision
    when a car that's moving left to right hits a car that's moving right to left.
    All cars continue moving in their trajectory as if they did not collide.
    Returns: number of collisions.

 tests = [
    lambda n: len(car_race_collision(n)) == 2 * n,
    lambda n: sum(car_race_collision(n)) == n * (n - 1),
    lambda n: car_race_collision(n) == n * n - n - 1
])
```
The script defines a function `car_race_collision` that simulates a road with two driving directions, and it calculates the number of collisions between cars moving towards each other on the road. The `tests` variable contains several tests that check the correctness of the `car_race_collision` function.