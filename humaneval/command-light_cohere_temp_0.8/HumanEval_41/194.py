```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    # Two sets of cars start out being very far from each other. All cars move in the same speed.
    # The will be considered that the first moving car hits the second moving car
    and stops, so there are now n-1 cars driving left to right. The remaining cars
    then continue moving in their trajectory as if they did not collide.
    # The function outputs the number of collisions.

test_collision = [1, 2, 4]
result = car_race_collision(test_collision)
print(result)
```