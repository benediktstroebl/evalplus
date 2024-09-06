```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars have in the same speed; two cars move toward collision
    when they meet. 

    cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

    return: 
    count_collisions = 0
    for i in range(n):
        if i == 0 or (i-1) % 2 == 0:
            for j in range(i):
                if j == i or (j-1) % 2 == 0:
                    count_collisions += 1
    return count_collisions
```