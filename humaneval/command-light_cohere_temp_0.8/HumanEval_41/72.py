```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed.
    Two cars intended to collide with each other. 

    when a moving car that's moving left to right hits a car that's moving right to left, the collision happens.
    then, the cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

    The function outputs the number of collisions.

test_collision = car_race_collision(10)
print(test_collision)

This function simulates the car race collision scenario, and the test_collision variable will store the number of collisions.