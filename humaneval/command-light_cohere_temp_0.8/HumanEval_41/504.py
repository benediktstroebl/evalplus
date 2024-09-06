Here's the self-contained Python function that solves the car-race collision problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Two cars are collide if they each car is moving
    at the same speed. They keep moving in the same direction.
    The function outputs the number of collisions.
"""
    def collision(self, left_speed, right_speed):
        """
        Determine if two cars move into collision
            based on their current speeds.
        """
        Parameters:
            - left_speed: int, Speed of the left car
            - right_speed: int, Speed of the right car
        """
        if left_speed == right_speed:
            return True
        else:
            return False
        return False
```
This function takes two arguments: `left_speed` and `right_speed`, representing the current speeds of the left and right cars, respectively.

The function checks whether the left and right speeds are equal. If they are equal, the function returns `True`, indicating a potential collision. If not, the function returns `False`, indicating that the cars are not moving into a collision. 

This function is self-contained and solves the car-race collision problem by determining whether the left and right cars are moving into a collision based on their current speeds.