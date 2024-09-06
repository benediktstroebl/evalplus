```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed; two cars will collide when moving into each other.
    The function outputs number of collisions.
    """
return sum(1 for i in range(n))  # single cars driving left to right collide with all others
"""

# Example of test
print(car_race_collision(10))
```
The function works by summing over all possible collisions of a single car driving left to right with all the other cars. This results in a number of collisions that will happen when the cars drive right to left.