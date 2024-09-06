```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    These two of cars start out being very far from each other. All cars move in the same speed.
    The cars have infinite durability, and as a result, they continue moving in their trajectory as if they did not collide.
    The function outputs the number of collisions that happen.
    """
return sum(1 for _ in itertools.collide(cars, cars[::-1]))
```