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

    :param n: The number of cars driving left to right and right to left.
    :return: The number of collisions.
    """
    # The key insight is that for each car driving right to left, it will collide with each car
    # driving left to right that is to its right, up to the nth car.
    # Therefore, the number of collisions is the sum of the number of cars to the right
    # of each car driving right to left.
    return sum(range(n))


# Test the function
print(car_race_collision(2))  # Output: 1
print(car_race_collision(3))  # Output: 3
print(car_race_collision(4))  # Output: 6
print(car_race_collision(5))  # Output: 10
```

This script works by summing the numbers from 1 to `n` (inclusive), which is equivalent to the number of collisions as described in the problem statement. The `range` function generates a sequence of numbers from 1 to `n`, and the `sum` function adds them all together.