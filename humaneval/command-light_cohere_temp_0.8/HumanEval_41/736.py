```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed; two cars, which are moving towards each other, collide and continue moving.
    The number of collisions is the length of the longest sequence of two cars colliding.
    """
function outputs the number of collisions.

# Driver one starts from the right
# Driver two starts from the left
# 1 -> Driver one hits Driver two => collides and stops
# 2 -> Driver two hits Driver one => collides and stops
# ...
# longest sequence is [2,1]
# That's 2 collisions
return 2
```