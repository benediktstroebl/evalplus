```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between two sets of cars
    moving in opposite directions on a straight line. The cars are infinitely sturdy
    and continue moving after a collision.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions.
    """
    # The formula for the number of collisions is n*(n-1) for a one-way road,
    # because for each car, it can collide with every other car. However, 
    # this problem has two sets of cars, so we need to calculate the combinations
    # for both sets and then sum them up.
    # The formula for two sets of cars can be derived as 2*n*(n-1) / 2 
    # which is equivalent to n*(n-1).
    return n * (n - 1)


# Test the function
print(car_race_collision(5))  # Output: 20
```

However, the derived equation was based on the assumption that the two sets of cars are separate (1-way road), if that's a two-way road where cars can collide with other cars going in their opposite direction then the correct formula is `n*n` because each car from one set can collide with any car from the other set. 

```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions between two sets of cars
    moving in opposite directions on a straight line.

    Args:
    n (int): The number of cars in each set.

    Returns:
    int: The total number of collisions.
    """
    return n * n


# Test the function
print(car_race_collision(5))  # Output: 25
```