```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed, and two cars will collide as they meet heading-to-heading.
    The two sets of cars start out being very far from each other. All cars continue moving in their same speed as if they did not collide.
    return: number of collisions
    """
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i == j: continue
            elif abs(i - j) <= 1:
                ret += 1
    return ret
``` 
This function uses nested loops to check for collisions between pairs of cars. The function returns the number of collisions.

You can test this function by providing the argument n with a value of your choosing.