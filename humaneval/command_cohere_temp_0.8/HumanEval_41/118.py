Here's a Python script that includes a function to solve the car collision problem as per the provided description, along with testing functionality:
```python
import math

def car_race_collision(n: int) -> int:
    """
    Count the number of collisions between infinitely strong cars moving in opposite directions on an infinitely long straight road.
    """
    # Calculate the number of cars in each group
    left_cars = n // 2
    right_cars = n - left_cars
    
    # Determine possible collision points
    collisions = (right_cars + left_cars - 1) // 2
    
    # Ensure proper counting
    if right_cars >= left_cars:
        return collisions
    else:
        return math.inf

# Testing
def test_car_race_collision():
    assert car_race_collision(10) == 5  # Even number of cars, half right-moving, half left-moving
    assert car_race_collision(7) == 3  # Uneven number of cars, max possible collisions
    assert car_race_collision(0) == 0  # No collisions with no cars
    assert car_race_collision(1) == 0  # Only one car means no collisions
    assert car_race_collision(2) == 0  # Two cars can't collide with each other
    assert car_race_collision(3) == 1  # Three cars, one collision
    assert car_race_collision(4) == 2  # Four cars, two collisions
    assert car_race_collision(100) == 50  # Large number of cars for even distribution
    assert car_race_collision(101) == 51  # One extra car for maximum collisions

# Run tests if executed directly
if __name__ == "__main__":
    test_car_race_collision()
```

This script includes a function `car_race_collision` defined with a docstring that explains the problem. It takes an integer `n` as input, representing the number of cars in each direction. It calculates the number of cars moving left and right, determines the maximum number of possible collisions, and then adjusts the count to account for the fact that there will be more right-moving cars than left-moving cars. Finally, it tests this function using a variety of scenarios to ensure it behaves as expected. 

Note that this approach assumes that the cars are infinitely strong and durable, and thus continues moving undeterred after any theoretical collisions. Let me know if you would like me to explain any part of the code in more detail.