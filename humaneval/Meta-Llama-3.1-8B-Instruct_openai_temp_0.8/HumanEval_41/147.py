```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # The number of collisions is given by the formula n*(n-1) for n >= 2
    # This is because each car from the left can collide with all the cars to the right of it
    # and there are n-1 cars to the right of any given car from the left
    # We don't need to consider the case for n = 0 or n = 1 because we know that there will be 0 collisions in these cases
    if n >= 2:
        return n * (n - 1)
    else:
        return 0

# Test the function
print(car_race_collision(0))  # Expected output: 0
print(car_race_collision(1))  # Expected output: 0
print(car_race_collision(2))  # Expected output: 2
print(car_race_collision(3))  # Expected output: 6
print(car_race_collision(4))  # Expected output: 12
```

This script defines a function `car_race_collision(n)` that takes an integer `n` as input and returns the number of collisions between `n` cars driving left to right and `n` cars driving right to left. The function uses the mathematical formula `n*(n-1)` to calculate the number of collisions for `n >= 2`. For `n = 0` or `n = 1`, the function returns 0, since there are no collisions in these cases. The script includes test cases to verify the correctness of the function.