```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    all cars have the unique speed. Two cars with matching speeds collide
   
    If a car that's moving left to right hits a car that's moving right to left, they continue moving
    in their trajectory as if they did not collide. 
    
    However, the cars are infinitely sturdy and strong, so the collision does not stop the cars. 
    Returns the number of cars that move into the intersection. 

    formula: The number of cars in the intersection = n*(n-1) 
    """
    collisions = n*(n-1) 
    return collisions

# testing
print(car_race_collision(10))
```