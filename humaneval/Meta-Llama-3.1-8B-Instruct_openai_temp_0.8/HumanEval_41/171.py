```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions.

    """
    # Since all cars are infinitely sturdy, a collision will occur whenever two
    # cars meet.  Since the cars in each direction are all moving at the same speed,
    # we can think of the problem as arranging two lines of n cars each.
    # The collision points will occur at the intersections of the two lines.
    # To find the number of intersections, we can use the fact that the number of
    # intersections of two lines is equal to the number of elements in the
    # intersection of their sorted index sets.

    # The index of the i-th car in the first line is (i + 1), since the cars are 1-indexed
    # from the perspective of the driver.  Similarly, the index of the i-th car in the second
    # line is (n - i).

    # Thus, the intersection of the sorted index sets is the set of all i such that (i + 1) = (n - i).
    # Solving for i, we get i = (n - 1) / 2.

    # However, because the index sets are open-interval closed-interval on the left, we need to subtract 1
    # from the number of intersections if n is odd.

    # If n is even, then the number of intersections is (n / 2).
    if n % 2 == 0:
        return n // 2
    # If n is odd, then the number of intersections is ((n - 1) / 2).
    else:
        return (n - 1) // 2

# Test cases
print(car_race_collision(1))  # Output: 0
print(car_race_collision(2))  # Output: 1
print(car_race_collision(3))  # Output: 1
print(car_race_collision(10))  # Output: 5
```

This script uses the mathematical concept of the intersection of two sorted index sets to solve the problem efficiently. It takes into account whether the number of cars is even or odd, adjusting the result accordingly.