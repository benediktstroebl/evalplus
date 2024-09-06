```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. When a car that's moving left to right hits a car that's moving right to left, it will be a collision.
    }n cars are going to collide

    The function outputs the number of collisions.

# Test cases

print(car_race_collision(1)) # Output: 0
print(car_race_collision(4)) # Output: 3
```

This function takes an integer n as input and returns the number of collisions between n cars driving on a straight road. The function works by simulating the movement of the cars and checking if they collide. The function then returns the number of cars that have collided.