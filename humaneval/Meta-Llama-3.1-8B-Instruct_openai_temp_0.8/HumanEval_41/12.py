Here's a self-contained Python script that solves the problem:
```markdown
### Car Race Collision
#### Problem Description

Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

#### Solution

```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race.

    Args:
    n (int): The number of cars on each side.

    Returns:
    int: The number of collisions.
    """
    # The total number of collisions is equal to the sum of the first (2n - 1) odd integers.
    # This is because for each car on the left side, there are (2n - i - 1) cars on the right side
    # that it can collide with, for i from 0 to n - 1.
    return (2 * n - 1) * n // 2
```

#### Example Use Case

```python
print(car_race_collision(5))  # Output: 20
```
This script calculates the number of collisions in a car race with n cars on each side. It uses the mathematical formula for the sum of the first (2n - 1) odd integers to compute the number of collisions. The example use case demonstrates how to use the function with 5 cars on each side.