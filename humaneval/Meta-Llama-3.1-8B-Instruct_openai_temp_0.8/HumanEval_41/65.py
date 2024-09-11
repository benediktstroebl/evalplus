```python
def car_race_collision(n: int):
    """
    Calculate the number of collisions in a car race with n cars moving left to right
    and n cars moving right to left on an infinitely long straight road.

    Args:
    n (int): The number of cars moving in each direction.

    Returns:
    int: The total number of collisions.
    """
    # Initialize the total number of collisions to 0
    total_collisions = 0
    
    # Generate all possible pairs of cars
    for i in range(n):
        for j in range(n):
            # If the cars collide, increment the total number of collisions
            # A car moving left to right will collide with a car moving right to left
            # if the left-to-right car's position is greater than the right-to-left car's position
            total_collisions += 1
    
    # Since we're counting each pair twice, divide the total by 2
    total_collisions = total_collisions // 2
    
    # However, we've also counted the pairs (i, i) for each i, where each car is its own pair
    # This is not a valid collision, so subtract n from the total
    total_collisions -= n
    
    return total_collisions


# Example usage:
n = 2
print(f"Number of collisions with {n} cars in each direction: {car_race_collision(n)}")
```

This script uses nested loops to generate all possible pairs of cars. It then increments the total number of collisions each time it finds a pair of cars that collide. However, since each pair is counted twice, it divides the total by 2. It also subtracts n from the total, because it counted each car as its own pair.