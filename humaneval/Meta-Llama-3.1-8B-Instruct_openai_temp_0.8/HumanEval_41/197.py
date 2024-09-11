### Car Collision Script
```python
def car_race_collision(n: int):
    """
    Calculate the number of car collisions in a simultaneous left-to-right and right-to-left car race.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The total number of car collisions.
    """
    # Calculate the total number of cars
    total_cars = 2 * n

    # The number of collisions is equal to the total number of cars minus 1
    # Because each car can only collide with the cars in the other direction
    collisions = total_cars - 1

    return collisions

# Example usage:
if __name__ == "__main__":
    n = 5  # Number of cars in each direction
    print(f"The number of car collisions in a race with {n} cars in each direction is: {car_race_collision(n)}")
```
This script uses the mathematical property that the total number of collisions is equal to the total number of cars minus 1. This is because each car can only collide with the cars in the other direction, not with itself or with cars in the same direction.