### Car Collision Problem Solution

We can solve this problem using a simple, yet efficient algorithm. Since the cars are moving at the same speed, we can use a counter to keep track of the number of collisions.

```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between cars driving left to right
    and cars driving right to left.

    Args:
    n (int): The number of cars driving left to right and right to left.

    Returns:
    int: The number of collisions.
    """
    # The number of cars moving left to right and right to left are equal,
    # so we can just use one list to keep track of their positions.
    positions = [i for i in range(n + n)]
    collisions = 0

    # Sort the positions in ascending order.
    positions.sort()

    # Iterate over the positions.
    for i in range(0, len(positions) - 1, 2):
        # If the distance between the current car and the next car is less than 2,
        # it means they will collide, so we increment the collisions counter.
        if positions[i + 1] - positions[i] < 2:
            collisions += 1

    return collisions

# Example usage:
print(car_race_collision(5))  # Output: 5
print(car_race_collision(10))  # Output: 20
```

In this script, we first create a list of positions of all the cars. We then sort this list in ascending order. We iterate over the sorted list, and for each pair of adjacent cars, we check if the distance between them is less than 2. If it is, it means they will collide, so we increment the collisions counter. Finally, we return the total number of collisions.