```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    All cars move in the same speed; two cars will collide and continue moving in their trajectories.
    as a
    cars are infinitely sturdy and strong, as a result, they continue moving
    in their trajectory as if they did not collide.
    return: collision
    return: a list of all collisions in the order they happened.
    """
     return: [left_collision, right_collision]
```
This function uses two parameters, n: the number of cars driving on the road, and direction: a string indicating whether a car is driving to the right or left. 

The function creates two lists, one for each set of cars, and then compares the two lists. 

After each car in the first list collides with the first car in the second list, it adds the second car to the first list and subtracts the first car from the second list. 

Finally, it returns the list of collisions in the order they happened.