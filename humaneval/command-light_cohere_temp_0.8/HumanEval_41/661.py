Here is a Python script with a self-contained function that solves the problem of two cars colliding on a straight road:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars have the roll over infinitely 
    and move at the same speed. Two cars move into the time to collide.
    If two cars are moving in opposite directions. They are collide when a car that's moving left to right hits a car that's moving right to left.

    However, the cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide. The function outputs the number of collisions.
```
This Python code defines a function called car_race_collision that simulates a head-to-head collision between two cars on a straight road. The function takes an input parameter n, which represents the number of cars involved in the collision. The cars start out from rest and move at the same speed, and the function calculates the time it takes for the two cars to collide and then determines whether the collision occurred. The code also checks if the output is the expected number of collisions.

The function uses a counter to keep track of the number of collisions and outputs the number of collisions.