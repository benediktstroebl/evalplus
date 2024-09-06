```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    Two cars meet the causes a collision.
    The number of cars colliding is the same as the number of cars.

Example:
    n = 3
    print(f"There are {n} cars on the road.")
    assert car_race_collision(n) == 3
    print("Cars are driving!")
    assert car_race_collision(n+1) == 0
    print("Cars have stopped.")
```