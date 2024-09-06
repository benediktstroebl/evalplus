```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed; two cars facing each other will collide.
    The cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.
    The function outputs the number of collisions
    """
    # Define the list of cars, with n cars driving each direction
    cars = [list([i]*n) for i in range(n)]

    # Use a generator expression to generate collisions based on the cars list
    for i, j in zip(cars, cars[::-1]):
        # Check if the current car is moving left to right and the next car is moving right to left
        if i[::-1] == j:
            yield i, j

    return len(cars)
```

This Python script defines a function `car_race_collision` that simulates a car race collision scenario with two sets of cars moving in opposite directions. The function uses a generator expression to generate collisions between pairs of cars that are facing each other, and then checks if the current car is moving left to right and the next car is moving right to left using the `cars` list. The `yield` statement generates the collision as a tuple containing the indices of the two cars. The `cars` list is used to create a circular movement of each car by starting it from the end of the `cars` list.