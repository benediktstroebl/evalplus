```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars move in the same speed; two cars will collide as they meet each other's heading while moving. 
    The function outputs the number of collisions.

return total_collisions = sum( [1 if n >= i*i else 0 for i in range(n)] )
``` 
This function is a self-contained implementation of the problem statement. It uses mathematical reasoning and a pattern of counting to solve the problem. The code is organized clearly and follows the standard Python function/method definition style.