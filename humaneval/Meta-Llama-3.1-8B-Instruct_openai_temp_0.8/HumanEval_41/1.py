```markdown
### Car Collision Count
#### Problem Statement

Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

#### Solution

This problem can be solved by considering each left-moving car and calculating the number of right-moving cars it can collide with. We can use the concept of "prefix sum" to efficiently calculate this in O(n) time complexity.

```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions between n pairs of cars moving in opposite directions.

    Args:
        n (int): The number of cars moving in each direction.

    Returns:
        int: The number of collisions.
    """
    # Calculate the total number of cars
    total_cars = n * 2

    # Initialize an array to store the prefix sum of the number of cars that can collide with each car
    prefix_sum = [0] * (n + 1)

    # Iterate over each car moving left to right
    for i in range(1, n + 1):
        # The number of cars that can collide with the current car is equal to the number of cars to its right
        # plus the number of cars that can collide with the car that is at the same position as the current car
        # when the current car moves one position to the right
        prefix_sum[i] = prefix_sum[i - 1] + (n - i + 1)

    # The total number of collisions is equal to the sum of the prefix sum
    return sum(prefix_sum)

# Example usage:
n = 5
print(f"Number of collisions when n = {n}: {car_race_collision(n)}")
```

This script defines a function `car_race_collision` that takes an integer `n` as input and returns the total number of collisions between `n` pairs of cars moving in opposite directions. The function uses a prefix sum array to efficiently calculate the number of collisions in O(n) time complexity.