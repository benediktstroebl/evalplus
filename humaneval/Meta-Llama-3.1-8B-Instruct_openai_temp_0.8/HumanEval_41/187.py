### Car Collision Simulation
#### Problem Statement:
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

#### Solution:
```python
def car_race_collision(n: int):
    """
    Calculates the number of car collisions.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions.
    """
    # Since each car is infinitely sturdy, we can consider each car as a "pole"
    # and calculate the number of intersections (collisions) using the formula:
    # The number of intersections is equal to the number of pairs of poles.
    # Since each pair is counted twice, we divide by 2.
    return n * (n - 1) // 2
```

#### Example Use Cases:
```python
print(car_race_collision(3))  # Output: 3
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10)) # Output: 45
```

This solution uses the concept of combinatorics to calculate the number of collisions. The formula `n * (n - 1) // 2` is a well-known formula for calculating the number of pairs of items from a set of `n` items.