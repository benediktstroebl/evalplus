```markdown
## Car Race Collision Problem Solution
### Problem Description

Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

This function outputs the number of such collisions.

### Solution
```python
def car_race_collision(n: int) -> int:
    """
    Returns the number of car collisions in a car race.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of car collisions.
    """
    # The total number of collisions is the square of the number of cars,
    # minus the number of cars, because each car collides with the other cars
    # in its own direction, but we don't count those collisions
    return n * n - n

# Example usage
print(car_race_collision(5))  # Output: 20
print(car_race_collision(10))  # Output: 100
```

### Explanation

The solution to this problem is based on the concept of combinations in combinatorics.
Each car can collide with every other car, and the number of cars that can collide
with a given car is equal to the number of cars in the other direction minus 1,
because a car cannot collide with itself.

The total number of collisions is therefore the product of the number of cars in
each direction, minus the number of cars, to avoid counting each car's internal
collisions. This is equivalent to the formula `n * n - n`, where `n` is the number
of cars in each direction.

This solution is efficient and scalable, as it only requires a constant amount of
computational work regardless of the input size. It also has a time complexity of
O(1), making it suitable for large inputs.