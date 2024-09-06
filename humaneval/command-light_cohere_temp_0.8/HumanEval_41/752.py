```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed. Two cars will meeting collide when a car that's moving left to right hits a car that's moving right to left.

    :return any number of collisions, if n is even
    """
    return n//2 if n%2 else n//2 + n%2

#Test cases
test_car_race_collision = [10,20]
test_car_race_collision(10) # 10 collisions
test_car_race_collision(20) # 20 collisions

#General script
```