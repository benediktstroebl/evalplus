```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed
    Two cars are driving towards each other, let's say they're moving in the same direction.
    When a car that's moving left to right hits a car that's moving right to left, a collision occurs.
    The two cars continue moving in their original direction, as if they did not collide.
    The function outputs the number of collisions that occurred.
    """
num_collisions = 0
    for i in range(n):
        # Create a tuple of the current time and the direction each car is driving
        car_tuple = (i, 1 - i)
        # Check if any tuple matches the direction of the leftmost car
        left_car = min(car_tuple, key=car_tuple[1])
        if left_car == car_tuple[0]:
            # If so, there was a collision
            num_collisions += 1
    return num_collisions

# Test the function
n = 10
result = car_race_collision(n)
print(result)
```