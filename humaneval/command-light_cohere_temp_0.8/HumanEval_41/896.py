```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Each car's same in the same speed. 
    Two cars are collide and move as if they did not.
    The function returns the number of collisions.

return n_collisions

# Your code goes here
n = int(input())
n_collisions = car_race_collision(n)
print(f'Total number of collisions: {n_collisions}')
```