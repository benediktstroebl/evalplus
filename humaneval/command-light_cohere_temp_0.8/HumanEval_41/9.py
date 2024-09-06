Here's the self-contained Python script that defines the function `car_race_collision` from the problem statement:

```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. 
    All cars have the final velocity.
    The function outputs the number of collisions
    """
    return sum(2**i for i in range(n))
```

This script defines a function that simulates the described scenario of cars moving on a straight road and colliding with each other. The function uses a formula to calculate the number of collisions, which is based on the concept of pairs of even numbers. 

The script is self-contained, as it does not rely on any external functions or modules, and it can be used directly as is.