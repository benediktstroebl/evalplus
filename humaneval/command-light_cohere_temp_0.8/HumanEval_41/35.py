Here's the improved Python script with the self-contained function 'solve_car_race_collision()' that addresses the problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    The two sets of cars start out being very far from each other. 
    All cars move in the same speed and direction, two cars will collide.
    The function outputs the collision number.
    """

Let's say we have 2 cars, the leftmost is moving at x1m/s and the rightmost is moving at x2m/s. The function works by calculating the time it takes for them to collide. The formula would be t = x2 - x1 / (x1 + x2) and then using that formula it calculates the time it takes for them to collide and then returns the collision count. 
Passing the test is simple: we just check if the time it took to collide is less than 0. If it is, the test passes.