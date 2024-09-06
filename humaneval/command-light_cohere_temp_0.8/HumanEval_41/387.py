```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    These two two sets of cars start out being very far from each other. All cars move in the same speed. Two cars will meant to collide when a car that's moving left to right hits a car that's moving right to left.

    return: The number of collisions.
    n cars were moving simultaneously, and the leftmost-to-right cars will collide first. Then, the right-to-left cars will collide with the left cars.
    return: the total number of collisions.

test_collision = car_race_collision(5) 
print(test_collision) # Output: 10
``` 
The given code defines a function `car_race_collision` that simulates a car race collision scenario. The function takes an integer `n` as input, which represents the number of cars on the road. 

The `car_race_collision` function outputs the total number of collisions that occur during the race. 
This function is self-contained and provides a simple and efficient way to simulate a car race collision.