### Car Collision Function
```markdown
## Problem Description
Given `n` cars moving left to right and `n` cars moving right to left, 
this function calculates the number of collisions between the two sets of cars.

## Assumptions
- All cars move at the same speed.
- Cars are infinitely sturdy and strong, so they continue moving after collision.

## Python Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving left to right and right to left.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions.
    """
    # The number of collisions is equal to the number of pairs that can be formed from n elements
    # This can be calculated using the combination formula: nC2 = n*(n-1)/2
    return n * (n - 1) // 2
```

## Example Usage
```python
print(car_race_collision(3))  # Output: 3
print(car_race_collision(5))  # Output: 10
```
In this solution, we use the fact that the number of collisions is equal to the number of pairs that can be formed from `n` elements. This can be calculated using the combination formula `nC2 = n*(n-1)/2`. The `//` operator is used for integer division to ensure the result is an integer.