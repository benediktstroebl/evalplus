```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario.

    Args:
    n (int): The number of cars driving left to right and right to left.

    Returns:
    int: The number of collisions between cars.
    """
    # Calculate the total number of possible collisions
    # Each car is a potential collision partner for all other cars
    total_collisions = n * (n - 1) // 2
    
    # Since the cars are traveling in opposite directions and don't change speed,
    # we can think of the possible pairs of cars as being divided into two groups:
    # pairs where the left-to-right car comes "first" and pairs where the right-to-left car comes "first".
    # In the case of the left-to-right car coming first, there are n possible choices for the left-to-right car,
    # and n choices for the right-to-left car (since it could be any of the cars except the one coming first).
    # However, in the case of the right-to-left car coming first, there are also n choices for the right-to-left car,
    # but only n-1 choices for the left-to-right car (since the left-to-right car cannot be the one coming "second").
    # Thus, the total number of possible collisions is ((n * n) + (n * (n - 1))) / 2 = n * (n - 1) / 2.
    # However, this is still not the total number of possible collisions, since each collision has been counted twice.
    # To get the total number of collisions, we need to divide this number by 2.
    
    # This can be simplified to n * (n - 1) // 2 which is the formula for combination 2
    # However, in order to account for both directions, we should do n * n 
    # The reason is because there are n cars traveling left to right and n cars traveling right to left.
    # When one car from either direction meets a car from the other, it's a collision.
    # So there are n possibilities for the left to right car and n possibilities for the right to left car.
    # Since each collision is counted twice, we divide by 2.
    total_collisions = n * n // 2
    
    return total_collisions

# Example usage:
print(car_race_collision(10))
```
This script takes an integer `n` representing the number of cars driving left to right and right to left, and returns the number of collisions between these cars.