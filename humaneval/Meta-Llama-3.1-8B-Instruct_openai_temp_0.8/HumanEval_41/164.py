### Car Collision Problem
#### Problem Description
Imagine a road that's a perfectly straight infinitely long line.
`n` cars are driving left to right; simultaneously, a different set of `n` cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

#### Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between cars driving in opposite directions.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    # Because the cars travel at the same speed, the number of collisions is
    # equivalent to the number of pairs of cars that can overlap.
    # This is equivalent to the number of ways to choose 2 cars from n.
    # The formula for the number of combinations is n! / (k!(n-k)!)
    # In this case, k = 2, so the formula simplifies to n(n-1).
    return n * (n - 1) // 2
```

#### Example Use Case
```python
# Calculate the number of collisions when 5 cars are driving in each direction.
print(car_race_collision(5))  # Output: 10
```
This solution uses the mathematical concept of combinations to calculate the number of pairs of cars that can overlap. The formula `n * (n - 1) // 2` calculates the number of ways to choose 2 cars from `n`, which is equivalent to the number of collisions.