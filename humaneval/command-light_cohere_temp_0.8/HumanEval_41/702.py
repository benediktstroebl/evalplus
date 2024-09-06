```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars have in the same speed; two cars will collide and move on their trajectory. 

    The function outputs the number of collisions. 

return count(n//2) * [2*n - 1]

#Testing
def test_car_race_collision():
    assert car_race_collision(3) == 2

```