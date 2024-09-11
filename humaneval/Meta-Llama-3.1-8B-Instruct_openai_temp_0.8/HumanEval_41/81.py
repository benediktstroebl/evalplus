### Car Race Collision Problem
#### Problem Description

Imagine a road that's a perfectly straight infinitely long line. `n` cars are driving left to right;  simultaneously, a different set of `n` cars are driving right to left. The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars are said to collide when a car that's moving left to right hits a car that's moving right to left. However, the cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

#### Solution

This problem can be solved using combinatorics.

```python
from math import comb

def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in the car race collision problem.

    Args:
    n (int): The number of cars driving left to right and right to left.

    Returns:
    int: The number of collisions.
    """
    # The number of collisions is equal to the number of ways to choose 2 cars from n, 
    # because each pair of cars can potentially collide.
    return comb(n, 2)

# Example usage:
n = 5
print(f"The number of collisions when n = {n} is: {car_race_collision(n)}")
```

In this script, we use the `math.comb` function to calculate the number of combinations of n items taken 2 at a time, which is equal to the number of potential collisions.