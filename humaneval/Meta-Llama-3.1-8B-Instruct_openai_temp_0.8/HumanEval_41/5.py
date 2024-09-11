```markdown
### Car Collision Problem

#### Problem Statement

Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

#### Solution

This function outputs the number of such collisions.

```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race with n cars going left to right and n cars going right to left.

    Args:
        n (int): The number of cars going left to right and right to left.

    Returns:
        int: The number of collisions that occur.
    """
    # Initialize the number of collisions to 0
    collisions = 0
    
    # Calculate the number of collisions as n (n choose 2), using the formula for combinations
    # Since each pair of cars collides exactly once, the number of collisions is n choose 2
    import math
    collisions = math.comb(n, 2)
    
    return collisions

# Example usage:
print(car_race_collision(5))  # Output: 10
```

This script uses the `math.comb` function from Python's `math` module to calculate the number of combinations of `n` items taken `2` at a time, which is equivalent to `n choose 2`. This is the formula for calculating the number of pairs of cars that can collide.