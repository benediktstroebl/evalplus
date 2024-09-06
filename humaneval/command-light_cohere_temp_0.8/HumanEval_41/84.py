```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed and direction, so the collision is a head-on collision, 
    where the front bumper of one car smashes into the front bumper of the other.
    The function returns the certain number of cars that are in the race, and returns the number of collisions.

# Example: test the function with different inputs
assert car_race_collision(6)
assert car_race_collision(8) == 10
```