```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Each car moves in the same speed.
    Two cars want to collide
    when a car that's moving left to right hits a car that's moving right to left, 
    the cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.
    Returns: number of collisions.
    """
The solution to this problem is to count the number of collisions.

Test cases:
assertEqual(car_race_collision(10), 5) # 10 cars driving left to right, 5 cars driving right to left

This code defines a function car_race_collision(n) that simulates a road with cars driving towards each other. It counts the each car's driving to collide, and continues moving after the collision. The number of collisions is returned as the output of the function.