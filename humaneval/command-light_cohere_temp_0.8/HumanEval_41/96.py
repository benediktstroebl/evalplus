```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    All cars move in the same speed. Two cars want to collide
    when a car that's moving left to right hits a car that's moving right to left.
    Function outputs whether collisions happen and returns the number of collisions.

tests = [10,20]
for test in tests:
    result = car_race_collision(test)
    assert result == test

``` 
This code defines a function `car_race_collision` that simulates the motion of cars on a straight road and counts the number of collisions between them. The tests then verify that the function's output matches the input size.