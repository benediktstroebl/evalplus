```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed and start out being very far from each other. 
    
    The function outputs the number of collisions.
    return the number of collisions.


    return sum( [1 for i in range(n)] * [n // 2] )
```