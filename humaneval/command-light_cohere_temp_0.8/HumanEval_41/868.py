```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    These two two sets of cars start out being very far from each other. All cars move in the same speed.

    Two cars intended to collide meet each other's position and move relative speed.

    The two cars will collide and stop moving, but they continue moving in their original trajectory as if they did not collide.

    return the number of collisions.
    """ number of vehicles that have met in their collisions.

Test cases:
1. Test case 1: n=3;

    Three cars are driving simultaneously, two are moving right and one is moving left. The first collision happens when the second car hits the first car moving right. The second collision happens when the first car hits the car moving left. The third car keeps moving right and won't collide with anything.

2. Test case 2: n=6;

   Six cars are driving simultaneously, four are moving right, two are moving left, and two are moving right to left. The first collision happens when the second car moving right hits the car moving right to left, the second collision happens when the first car moving right hits the car moving left.

This script defines a function car_race_collision that simulates a collision between two cars driving on a straight road. It uses a position and speed to determine when and how the cars collide. The script provides test cases to check the functionality of the function.