### Collisions in a Car Race
#### Problem Description

Imagine a road that's a perfectly straight infinitely long line. `n` cars are driving left to right;  simultaneously, a different set of `n` cars are driving right to left. The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars are said to collide when a car that's moving left to right hits a car that's moving right to left. However, the cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

#### Solution

```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions in a car race with n cars
    moving left to right and n cars moving right to left, assuming the cars are
    infinitely sturdy and strong.

    Args:
    n (int): The number of cars driving left to right and right to left.

    Returns:
    int: The total number of collisions.
    """
    # Since each car is infinitely sturdy, we can think of each pair of cars
    # as a single collision point. The first n cars can collide with the last
    # n cars, then the second last cars, and so on.
    # Therefore, the total number of collisions is n * (n - 1) // 2
    collisions = (n * (n - 1)) // 2
    return collisions

# Test the function
print(car_race_collision(3))  # Output: 3
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10)) # Output: 45
```

This function uses a mathematical approach to calculate the number of collisions, which simplifies the problem by considering each pair of cars as a single collision point. The time complexity of this function is O(1), making it efficient for large inputs.