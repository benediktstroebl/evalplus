```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a straight infinitely long road race.

    Args:
        n (int): The number of cars moving left to right and right to left.

    Returns:
        int: The number of collisions between the two sets of cars.
    """
    # The total number of possible collisions is the sum of the numbers from 1 to n
    # This is because each car that's moving left to right can potentially collide with all cars that are moving right to left
    total_collisions = n * (n + 1) // 2

    return total_collisions

# Example usage:
n = 5
print(f"Number of collisions for n = {n}: {car_race_collision(n)}")
```

In this script, we use the mathematical formula for the sum of the first n positive integers to calculate the total number of possible collisions. This formula is `n * (n + 1) / 2`, which is implemented in the `total_collisions` variable. We then return this value from the `car_race_collision` function.

The example usage at the end shows how to use this function with `n = 5`, and prints the result to the console.