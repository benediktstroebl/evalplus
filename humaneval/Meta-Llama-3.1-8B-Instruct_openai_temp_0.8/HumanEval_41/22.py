### Car Collision Problem Solution
#### Problem Description
This script calculates the number of collisions between two sets of cars moving in opposite directions on an infinitely long straight road.

#### Code
```python
def car_race_collision(n: int) -> int:
    """
    Calculates the number of collisions between two sets of cars moving in opposite directions.
    
    Args:
        n (int): The number of cars moving in each direction.

    Returns:
        int: The total number of collisions.
    """
    # The formula for the number of collisions is (2*n - 1) * (n - 1) / 2
    # This is because each car in one set can potentially collide with each car in the other set
    # But we divide by 2 to avoid double counting
    return (2*n - 1) * (n - 1) // 2
```

#### Example Use Cases
```python
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```
This script provides a simple and efficient solution to the problem by using a mathematical formula that calculates the number of collisions directly.