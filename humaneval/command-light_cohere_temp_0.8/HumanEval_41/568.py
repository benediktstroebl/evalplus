```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    Each car has a same constant speed and direction, so they will collide
    if they meet. Two cars that are moving towards each other will collide
    when one car that's moving left to right hits a car that's moving right to left.
    If cars are infinitely sturdy and strong, as a result, they continue moving
    in their trajectory as if they did not collide.

    return the collision is the number of collisions that happen.
    """
The function returns the number of collisions.

test_collision = car_race_collision(3)

print(test_collision)
```