```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars move in the same speed and direction; 
    The function outputs the number of collisions.
    """return 2*(n*(n-1)) // (n*(n-2))
```