```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race scenario.

    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    # The number of collisions is equal to the number of ways to select 2 cars from a set of n,
    # because each pair of cars can collide. This is a combination problem.
    # We use the formula for combination: n choose 2 = n * (n - 1) / 2
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    else:
        return n * (n - 1) // 2

# Example use case:
n = 5
print(f"The number of collisions when n = {n} is: {car_race_collision(n)}")
```

In this script, we define a function `car_race_collision(n)` that calculates the number of collisions in a car race scenario with `n` cars moving left to right and `n` cars moving right to left. The function uses the formula for combination to calculate the number of pairs of cars that can collide, which is equal to the number of collisions. The example use case shows how to use the function with `n = 5`.