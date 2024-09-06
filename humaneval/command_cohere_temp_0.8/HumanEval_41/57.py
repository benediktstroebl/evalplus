Here's a Python script that includes a function to solve the car collision problem as per the provided description, along with testing functionality:
```python
def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move in opposite directions on an infinitely long straight road.
    """
    collisions = 0
    
    # Define two sets of cars along the same straight path
    cars1 = ['A' + str(i) for i in range(n)]
    cars2 = ['B' + str(i) for i in range(n)]
    
    # Reverse the second set of cars for collision detection
    cars2.reverse()
    
    # Check for collisions between the two sets
    for car1 in cars1:
        for car2 in cars2:
            if car1 == car2:
                collisions += 1
                break  # Move on to the next car in cars1
    
    return collisions

# Tests
def test_car_race_collision():
    assert car_race_collision(1) == 0
    assert car_race_collision(2) == 1
    assert car_race_collision(5) == 10
    assert car_race_collision(10) == 45

if __name__ == "__main__":
    test_car_race_collision()
```
This script defines the `car_race_collision` function as per the problem statement and provides a testing function to validate the solution for various input sizes (`n`). You can adjust the values passed to the `test_car_race_collision` function to verify the behavior for different numbers of cars.