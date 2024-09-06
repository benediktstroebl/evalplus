```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    All cars move in the same speed and start out from the same location.
    The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.
    Returns the number of collisions.

test_collision = car_race_collision(5)
 assert test_collision == 4  # This should be correct, each car collides with the other 4 cars only once

# Example:
print(car_race_collision(10))  # Should print 10, as all 10 cars collide with each other 9 times.