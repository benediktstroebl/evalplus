```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions between two sets of n cars.
    The cars are driving in opposite directions on an infinitely long straight road.
    The function assumes that all cars move at the same speed.

    Parameters:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions.
    """
    # Each pair of cars from opposite directions will collide exactly once.
    # So, the total number of collisions is the number of ways to choose 2 cars from n (for one direction),
    # which is calculated using the combination formula: n choose 2.
    collisions = n * (n - 1) // 2

    # Since there are two sets of cars, we multiply the number of collisions by 2.
    return 2 * collisions


# Example usage:
n = 5
print(f"Number of collisions with {n} cars in each set: {car_race_collision(n)}")
```

This script defines the `car_race_collision` function, which takes the number of cars in each set as input and returns the total number of collisions. It uses the combination formula `n choose 2` to calculate the number of collisions between one set of cars and then multiplies it by 2 to account for the collisions with the other set of cars. Finally, it provides an example usage of the function with 5 cars in each set.