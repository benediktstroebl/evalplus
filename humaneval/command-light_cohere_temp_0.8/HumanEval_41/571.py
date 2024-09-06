```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed. Two cars facing each other collide and continue moving in their trajectory as if they did not.

    return: the number of collisions
    """
    n = n // 2 #Make sure n is odd to ensure all n cars have a turn
    before the last car moves

    return sum( [i == n - i -1 for i in range(n)])

# Test the function
assert car_race_collision(5) == 10
```