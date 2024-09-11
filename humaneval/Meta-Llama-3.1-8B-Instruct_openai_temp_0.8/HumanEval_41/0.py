```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions in a car race scenario.
    
    Parameters:
    n (int): The number of cars driving in each direction.
    
    Returns:
    int: The total number of collisions.
    """
    # The number of collisions is equal to the sum of the first n positive integers
    # because each car on the left will collide with each car on the right.
    # This is equivalent to the formula for the sum of an arithmetic series: n*(n+1)//2
    return n * (n + 1) // 2

# Example usage:
n_cars = 5
print(f"There will be {car_race_collision(n_cars)} collisions.")
```

This script uses the mathematical formula for the sum of the first n positive integers to calculate the number of collisions. The formula is n*(n+1)//2, where // is integer division (which discards the remainder and returns the quotient as an integer). The function takes an integer n as input, representing the number of cars driving in each direction, and returns the total number of collisions.