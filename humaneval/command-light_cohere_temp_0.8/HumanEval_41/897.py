Here is a Python script that includes a self-contained function to solve the problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. The cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

    Returns: number of collisions.
"""
    collisions = 0
    for i in range(n):
        for j in range(n):
            if i > j and i + j <= n:
                # The car moving right to left hits the car moving left to right
                collisions += 1
    return collisions

# Test cases
test_cases = [60, 50, 40]
for i, n in test_cases:
    expected = i * (n - 1) // 2
    result = car_race_collision(n)
    print(f"Test {i}: Expected: {expected}, Actual: {result}")
```

This script defines a function that simulates a car race collision scenario, where two sets of cars are driving towards each other on a straight road. The function counts the collisions between the cars and returns the total number of collisions. The test cases provided demonstrate how the expected collisions are calculated based on the problem statement.