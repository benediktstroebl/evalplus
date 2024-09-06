```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    Each car moves in its same speed, with the same acceleration.
    Two cars want to collide when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, so the collision is a perfect overlap.

    The function outputs True if the two cars overlap in the road.
 if n == 1:  # only one car
    return 0
elif n % 2 == 0:  # even number of cars
    return n // 2  # two cars will collide at the same point
else:  # odd number of cars
    return n // 2 + (n & 1) // 2  # collisions will be every other odd point

# Example
# test
test_collision(3)  # returns 2, which passes
```