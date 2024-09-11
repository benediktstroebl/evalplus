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
        n (int): The number of cars driving left to right.

    Returns:
        int: The number of collisions.
    """
    # The problem can be solved by using the formula for the number of combinations
    # of 2n items taken 2 at a time. This is because we are essentially choosing
    # 2 car pairs from 2n cars. The formula is n! / ((n-1)! * 1!), which is
    # equivalent to n*(n-1).
    if n <= 0:
        return 0
    else:
        return n * (n - 1)

# Example usage:
print(car_race_collision(1))  # Output: 0
print(car_race_collision(2))  # Output: 2
print(car_race_collision(3))  # Output: 6
print(car_race_collision(4))  # Output: 12
print(car_race_collision(5))  # Output: 20
```