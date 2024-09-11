### Car Collision Problem Solution
```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario.
    
    Parameters:
    n (int): The number of cars driving left to right and right to left.
    
    Returns:
    int: The number of collisions.
    """
    # Calculate the number of collisions using the formula n * (n-1) / 2
    # This is because each of the n cars can collide with all n-1 cars on the opposite side
    # Since order doesn't matter, we use the combination formula nC2 = n * (n-1) / 2
    collisions = n * (n - 1) // 2
    
    return collisions

# Example usage:
n = 5
print(f"The number of collisions when n = {n} is: {car_race_collision(n)}")
```

This Python script calculates the number of collisions in a car race scenario where n cars are driving left to right and n cars are driving right to left. It uses the combination formula nC2 to calculate the number of collisions, where order doesn't matter since the cars are infinitely sturdy and continue moving in their trajectory after collision. The example usage demonstrates how to call the function with n = 5 and print the result.