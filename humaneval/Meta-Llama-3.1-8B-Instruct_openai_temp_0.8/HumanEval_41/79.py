### Car Race Collision Problem
#### Problem Description
Imagine a road that's a perfectly straight infinitely long line. `n` cars are driving left to right; simultaneously, a different set of `n` cars are driving right to left. The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars are said to collide when a car that's moving left to right hits a car that's moving right to left. However, the cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

#### Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions.
    """
    # Observe that the cars will collide at positions x, x+1, x+2,..., 2n-1, x+n, x+n+1,..., 3n-1
    # where x is some non-negative integer.
    # These positions are the sum of the first k cars in the left-to-right set and k cars in the right-to-left set.

    # To count the number of collisions, we need to count the number of unit intervals [x, x+1], [x+n, x+n+1],...
    # where there are at least two cars in each interval. We also need to count the number of unit intervals [x, x+1],...
    # where there are at least one car in each interval.

    # The number of unit intervals where there are at least two cars is n-1 + n-2 +... + 1 = n*(n-1)/2.
    # The number of unit intervals where there are at least one car is n + n-1 +... + 1 = n*(n+1)/2.

    # However, the number of unit intervals where there are at least two cars includes the cases where there are at least three cars.
    # To count the number of collisions, we need to subtract the number of unit intervals where there are at least three cars.
    # The number of unit intervals where there are at least three cars is n-2 + n-3 +... + 1 = n*(n-1)/2 - (n-1)*(n-2)/2.

    # Thus, the total number of collisions is n*(n+1)/2 - n*(n-1)/2 + n*(n-1)/2 - (n-1)*(n-2)/2.
    # Simplifying the expression, we get n*(n+1)/2 - n*(n-1)/2 = n.

    return n

# Test the function
print(car_race_collision(1))  # Output: 1
print(car_race_collision(2))  # Output: 2
print(car_race_collision(3))  # Output: 3
```
This script uses mathematical reasoning to calculate the total number of collisions. It takes as input the number of cars `n` in each set, and returns the total number of collisions. The time complexity is O(1), making it efficient for large inputs.