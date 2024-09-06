```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. All cars move in the same speed.
    Two cars intended to collide
   
    When a car that's moving left to right hits a car that's moving right to left, the two cars will continue moving in their trajectory as if they did not collide.
    The number of collisions is returned
    """
    return sum(1 for x in range(n)) // returns the number of collisions

# Test the function
n = int(input("Enter the number of cars: "))
print("The number of collisions:", car_race_collision(n))
```