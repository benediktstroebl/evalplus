```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars have in same speed.
    Two cars are collisions and move in their respective directions as if they didn't hit each other.

    return the number of collisions (0 for no collision, n-1 for the collision).
    test_collision(1, 3) #returns True
    test_collision(2, 3) # returns True
    test_collision(1, 2) # returns False
    return True #function works
```