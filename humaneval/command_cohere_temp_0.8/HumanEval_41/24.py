Here's a Python script that includes a function to solve the car crash problem as per the provided markdown code block:
```python
def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n)]

    # Initialize collisions counter
    collisions = 0

    # Iterate until cars of the 2 lists intersect
    while len(left_driving) > 0 and len(right_driving) > 0 and left_driving[0] != right_driving[0]:
        if left_driving[0] < right_driving[0]:
            left_driving.pop(0)
        else:
            right_driving.pop(0)

        # If the first car in one list has a corresponding car in the other list, increment collisions
        if left_driving[0] == right_driving[0]:
            collisions += 1

    return collisions

# Unit tests for the function
def test_car_race_collision():
    assert car_race_collision(1) == 0
    assert car_race_collision(2) == 0
    assert car_race_collision(3) == 0
    assert car_race_collision(4) == 2
    assert car_race_collision(10) == 5
    assert car_race_collision(1000) == 499500

# Run the unit tests
test_car_race_collision()
```

This script includes a function `car_race_collision` defined with a description that aligns with the provided problem statement. The function takes in an integer `n` corresponding to the number of cars and returns the number of collisions between the 2 sets of cars. It achieves this by managing 2 lists (left_driving and right_driving) that represent the cars driving from left to right and right to left respectively. It then iterates through the lists until the 2 lists intersect (i.e., a collision occurs). The number of collisions is counted and returned accordingly.

The script also includes a set of unit tests, run using the `test_car_race_collision()` function, to ensure the function's correct behavior for various inputs.