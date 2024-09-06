```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    # as theytt two sets of cars start out being very far from
    each other. All cars move in the same speed, and two cars are heading
    toward each other to collide.
    # When two cars have perfectly elastic collisions, and continue moving in their
    original direction
    after colliding.
    return len([i for i,j in zip(range(n), range(n)) if i == j])
```