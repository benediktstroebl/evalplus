```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and start position.
    When cars move they by their starting position and speed, they will collide. 
    The function determines the number of collisions and returns that number.
    """

test_collision = car_race_collision(5)
assert test_collision == 4
```