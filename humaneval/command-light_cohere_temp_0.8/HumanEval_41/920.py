```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed
    Two cars will collide when a car that's moving left to right hits a car that's moving right to left.
    The function outputs the collisions that have happened.

    return:
    list of tuples, each tuple containing:
    int: index of a car that collided
    car_pos: tuple (x, y) representing the position of the car after collision
    """
    return [tuple(map(int, position)) for position in [[0, 1], [1, 0], [0, 1]] * n]
```