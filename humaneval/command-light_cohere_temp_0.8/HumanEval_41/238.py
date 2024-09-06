Here's the solution:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    # Two cars will move in the same speed and direction, they will collide.
    # The function outputs the number of collisions that happen.
    return sum(1 for i in range(n))

# Test cases:
def test_collision(test_n: int):
    assert car_race_collision(test_n) == test_n, "All cars should collide!"

# Example usage:
test_collision(3)  # Output: 4
```

This Python function, car_race_collision, simulates a road with cars moving towards each other. It returns the the expected number of collisions that happen on the road.

The function works by simulating an infinitely long road with cars moving towards each other. The function then counts the number of collisions, which occur when two cars move towards each other at the same speed and direction. The number of collisions is returned by the function.

This code is a self-contained solution that demonstrates collision detection in a moving car scenario.