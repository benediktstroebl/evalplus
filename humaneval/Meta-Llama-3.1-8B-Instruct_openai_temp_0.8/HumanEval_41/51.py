### Car Collision Problem Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between left-to-right and right-to-left cars.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    # The total number of cars is 2n
    total_cars = 2 * n
    
    # In a linear scenario, the only way for 2 cars to collide is if their indices
    # are complementary (i.e., i + j = total_cars - 1), where i is the index of a
    # left-to-right car and j is the index of a right-to-left car.
    
    # Therefore, we need to calculate the number of pairs of complementary indices
    # that exist among all the cars.
    
    # The number of pairs of complementary indices is equal to the number of pairs
    # of indices of the type (total_cars - 1 - i, i), due to the bijection
    # between (i, j) and (j, i).
    
    # This is given by the sum of the first n natural numbers, which we can
    # calculate using the formula n*(n+1)/2.
    
    collisions = n * (n + 1) // 2
    
    return collisions

# Example usage:
n = 5
print(f"Number of collisions with {n} cars in each direction: {car_race_collision(n)}")
```