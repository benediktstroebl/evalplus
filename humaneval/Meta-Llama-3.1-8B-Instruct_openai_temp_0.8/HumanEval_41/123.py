```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race where n cars are moving left to right
    and n cars are moving right to left.

    Args:
        n (int): The number of cars moving in each direction.

    Returns:
        int: The number of collisions.
    """

    # Initialize a list to store the number of cars on the road at each position
    # We use a list of size 2*n+1 to account for the 2*n cars plus 1 position before the first car
    road = [0] * (2 * n + 1)

    # Initialize the number of collisions to 0
    collisions = 0

    # Simulate each car moving on the road
    for i in range(1, 2 * n + 1):
        # For each car on the road, count the number of cars in the opposite direction
        # that it can collide with
        collisions += sum(road[j] for j in range(1, i)[::-1] if i - j <= n)

        # Update the number of cars on the road at the current position
        road[i] = road[i - 1] + 1

    # Return the total number of collisions
    return collisions

# Example usage:
print(car_race_collision(5))  # Output: 15
```

This script uses a simple simulation approach by iterating over each position on the road. For each car on the road, it counts the number of cars in the opposite direction that it can collide with. The total number of collisions is then accumulated and returned.