```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed. Two cars moving to collide will be those that are moving in opposite directions.
    The cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    return: 
    counter = 0
    for i in range(n):
        if i%2 == 0:
            for j in range(i):
                if j%2 == 0:
                    counter += 1
    return counter
```