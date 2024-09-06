```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed. A car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.
    Return the number of collisions.
    """ The number of cars in the road that are moving left to right
    """
    return 2*n + sum(n//2 for i in range(n))
```
The function first computes the number of cars driving left and adds the count of cars driving right. 

It also calculates the total number of cars in the road by summing the result of the thread of evenly distributed cars moving right. 

Finally, it returns the total number of collisions.