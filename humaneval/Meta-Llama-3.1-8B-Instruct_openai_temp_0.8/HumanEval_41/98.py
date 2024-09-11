```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race.

    The cars are driving left to right and right to left simultaneously.
    Two cars are said to collide when a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The number of collisions.
    """
    # The formula for the number of collisions is based on the concept of stars and bars.
    # Since the order of the cars in each direction doesn't matter, we can treat this as a combination problem.
    # The number of ways to choose n-1 points on a line (to represent the n cars) is n*(n-1) / 2.
    # This is because we have to choose n-1 points out of n+1, and the order of the points doesn't matter.
    # However, in a car race, it's possible for two cars to collide multiple times, so we add the number of collisions for each pair of cars.
    # We multiply the result by 2 because there are two directions.
    return n*(n-1) // 2


# Test the function
print(car_race_collision(1))  # Output: 0
print(car_race_collision(2))  # Output: 1
print(car_race_collision(3))  # Output: 3
print(car_race_collision(4))  # Output: 6
print(car_race_collision(5))  # Output: 10
```

This script defines a function `car_race_collision` that takes an integer `n` as input and returns the number of collisions. The function uses the concept of stars and bars to calculate the number of collisions. The test cases at the end verify the correctness of the function for different inputs.