```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed, and the cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.

    return a number of collisions
    """
    # Set of cars: Each car is represented as a list of numbers [left,right], representing its starting and ending positions.
    cars = [[0,0] * n, [n-1,0] * n] 
    
    # The first car is always at 0,0.
    car_index = [0]* n
    car_index = [0]* n
    
    # First car hits second car, so it stops.
    for i in range(n):
        if car_index[i][0] == car_index[i][1]:
            break
        # If the first car stops, then the second car is moving into its space.
        car_index[i][1] += 1
        car_index[i][0] += 1
        car_index[i][1] -= 1
        car_index[i][1] += 1

    # Now, the second car has stopped, and the first car is moving into its space.
    for i in range(n):
        if car_index[i][0] == car_index[i][1]:
            break
        # If the second car stops, then the first car is moving into its space.
        car_index[i][0] += 1
        car_index[i][1] -= 1
        car_index[i][0] += 1
        car_index[i][1] += 1

    # If they both pass this point, there are no collisions.
    return sum(car_index)
```
This Python script defines a function car_race_collision that simulates a collision of n cars on a road. The function works by creating a set of n cars, with each car represented as a list of starting and ending positions. The cars are then compared to each other to determine if they have collided, and the function returns the number of collisions.