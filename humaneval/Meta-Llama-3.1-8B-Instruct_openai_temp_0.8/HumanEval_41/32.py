```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions between two sets of n cars.
    
    Args:
    n (int): The number of cars in each set.
    
    Returns:
    int: The number of collisions.
    """
    return n * (n - 1)

# Test the function
print(car_race_collision(5))  # Example usage
```

This script works by noting that each car in the left-moving set will potentially collide with every car in the right-moving set, except for itself.  Since each car in the left-moving set is paired with every other car in the right-moving set, we don't need to multiply the number of cars in each set by the number of cars in the other set.  We can simply multiply the number of cars in one set by the number of cars in the other set, minus one (to exclude the car's self-collision).