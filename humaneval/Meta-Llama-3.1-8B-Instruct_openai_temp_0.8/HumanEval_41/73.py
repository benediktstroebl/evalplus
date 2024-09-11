```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race scenario.

    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.

    Args:
    n (int): Number of cars in each direction.

    Returns:
    int: Number of collisions.
    """
    # The number of collisions will be the sum of the first n-1 natural numbers
    # (0 + 1 + 2 +... + n-1) which can be calculated using the formula n*(n-1)/2
    # This is because each car in the left-to-right direction will collide with all
    # the cars in the right-to-left direction except for the last one.
    return n * (n - 1) // 2

# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

In this script, we calculate the number of collisions by using the formula for the sum of the first n-1 natural numbers, which is n*(n-1)/2. This is because each car in the left-to-right direction will collide with all the cars in the right-to-left direction except for the last one.