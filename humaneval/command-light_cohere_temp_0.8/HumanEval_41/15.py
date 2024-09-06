Here's the Python script with the self-contained function:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed.
    Two cars are collision when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.
    The function returns True if the total number of collisions is 0.
    """
    function returns a number of the collisions
"""
return sum([1 for car1, car2 in zip([range(n)] * [range(n)]) if car1 > car2])
```
The function counts the number of collisions by iterating over all possible pairs of cars and checking if one car is going in the opposite direction of the other. This results in a total number of collisions. The function then returns the total number of collisions as an integer.