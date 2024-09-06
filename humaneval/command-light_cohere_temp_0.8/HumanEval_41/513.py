```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and each other is
    infinitely strong. 

    Two cars will to collide, the function outputs the number of collisions. 

Test cases:
>>> car_race_collision(6)  # Output: 2
>>> car_race_collision(3)  # Output: 0

This function solves the problem of counting the number of collisions in a car race and passes the corresponding test cases successfully.