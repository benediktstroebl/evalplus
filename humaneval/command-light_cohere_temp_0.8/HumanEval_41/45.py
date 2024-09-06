```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    # Two sets of cars start out being very far from each other. All cars move in the same speed.
    # The cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.
    # This unique collision detection function
    returns the number of cars that were moving to the right and hit a car moving to the left.
    return: number of collisions
"""

This function works by counting the number of cars that are moving to the right and hit a car moving to the left. It does this by checking if the left-moving car is currently at the front of a right-moving car, and if so, counting the right-moving car as a collision.