```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of car collisions in a straight infinitely long road.
    
    Args:
        n (int): The number of cars driving left to right and right to left.
    
    Returns:
        int: The total number of car collisions.
    """
    # Calculate the total number of pairs of cars that can collide
    # This is done by using the formula for combinations: nC2 = n * (n - 1) / 2
    # Since each pair of cars can collide with each other, we get the total number of collisions
    total_collisions = n * (n - 1) // 2
    
    return total_collisions

# Test the function
print(car_race_collision(5))
print(car_race_collision(10))
print(car_race_collision(20))
```

This Python script defines the `car_race_collision` function to calculate the total number of car collisions given the number of cars driving left to right and right to left. It uses the formula for combinations to calculate the total number of pairs of cars that can collide. The test cases at the end demonstrate how to use this function with different inputs.