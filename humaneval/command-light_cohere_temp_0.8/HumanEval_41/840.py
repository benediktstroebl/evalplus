```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    As the cars are infinitely sturdy and strong, as a result, they continue moving
    in their trajectory as if they did not collide.

    return: 
        collides = []
        for i in range(n):
            # Define a car is moving to the left
            moving_left = False
            # Move it right
            car_right = i % n
            if car_right < n:
                collides.append((car_right, car_right))
            else:
                collides.append((car_right, n-1))
        return collides
```
The function `car_race_collision` simulates a road with two directions of movement, `left` and `right`. It keeps track of the cars moving in both directions, and when a car moving to the left hits another car moving right, they both are recorded in a list of collisions.