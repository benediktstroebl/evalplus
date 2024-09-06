Here's the code:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars are collide when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    return:
    - number of collisions
    - The number of cars that were moving
    left to right that collide with cars that are moving right to left
    - The number of cars that are moving right to left that collide with cars that are moving left to right

This script defines a function that simulates a road with two lanes of cars moving towards each other. It calculates the how many cars are moving, and then it determines if the cars collide. The function returns the number of collisions that occurred, which is the number of cars that were moving towards the right lane that hit a car moving left to right.