### Car Race Collision Problem Solution
```markdown
## Problem Description
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

## Solution
This function uses the concept of combinatorics to find the number of collisions.

```python
from math import comb
from math import sqrt

def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race.

    Parameters:
    n (int): The number of cars in each set.

    Returns:
    int: The number of collisions.
    """
    if n <= 1:
        return 0

    max_collision = n - 1
    return int((n * max_collision) / 2)
```

### Example Use Cases
```python
print(car_race_collision(1))  # 0 collisions
print(car_race_collision(2))  # 1 collision
print(car_race_collision(3))  # 3 collisions
print(car_race_collision(4))  # 6 collisions
print(car_race_collision(5))  # 10 collisions
```

### Explanation
The number of collisions is equal to the number of pairs of left-to-right cars that can collide with right-to-left cars. Since there are `n` left-to-right cars, the number of such pairs is `(n * (n - 1)) / 2`.

Note that this formula represents the number of combinations of `n` items taken 2 at a time, which is equivalent to the number of pairs of left-to-right cars that can collide with right-to-left cars.

This approach provides an efficient and accurate solution to the problem, handling cases with up to `n` cars in each set.