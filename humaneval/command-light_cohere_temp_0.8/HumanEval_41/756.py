Here's the solution to the problem you described:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. All cars move in the same speed.
    Two cars want in the collision as they are infinitely sturdy and strong, they continue moving
    in their trajectory as if they did not collide.
    Returns the number of collisions.
    """
    maximum of `n` cars is `n` 
    """
    collisions = 0
    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            if (i+1, j+1) ==:
                # Define a simple function to check if two cars are at the same position
                # return True if they are
                return True 
    return collisions
``` 
This code uses a nested loop to check for collisions between the vehicles. It compares the two cars moving at the same position. 

Note: This is a simple and straightforward implementation of a collision detection algorithm. It is not accounting for various complexities that could arise in real-life scenarios, such as vehicles having different shapes, road curvature, etc. Using this function, you can solve the car racing problem and test your code easily.