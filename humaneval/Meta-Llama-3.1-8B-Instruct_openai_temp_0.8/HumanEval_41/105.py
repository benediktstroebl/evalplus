### Car Race Collision Problem Solver
#### Problem Statement
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

This function outputs the number of such collisions.

#### Solution
```python
import math

def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions.
    """
    # The number of collisions is given by the number of pairs of cars from the two sets
    # This can be calculated using the formula for combinations: nC2 = n*(n-1)//2
    if n == 1:
        return 0
    else:
        return n*(n-1)//2

# Test the function
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
print(car_race_collision(20))  # Output: 190
```
This function takes an integer `n` as input, representing the number of cars in each direction. It then calculates the number of collisions using the formula for combinations: `n*(n-1)//2`. If there is only one car in one direction, there are no collisions.