Here is a Python script that includes a self-contained function to solve the car race collision problem:

```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Each car moves in the same speed.

    When two cars are moving in opposite directions hit each other,
    so they "feather" apart and continue moving in their original direction.

    The function outputs a number of collisions.
```

The function first creates two lists of equal length, n, representing the cars. Then, it iterates through the cars in the list and checks if the current car is driving in the opposite direction to the other car. The function then checks if the current car is driving to the right and the other car is driving to the left, it assumes a collision and subtracts one from the other car's position.