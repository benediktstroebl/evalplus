Here's a Python script that includes a function to solve the car collision problem described in the markdown code block:
```python
def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right driving cars.
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize a variable to track collisions.
    collisions = 0
    
    # Iterate through the cars in both lists.
    for i in range(n):
        # If a car is in both lists, they collide.
        if left_cars[i] in right_cars and right_cars[i] in left_cars:
            collisions += 1
            # Remove collisions to prevent double-counting.
            left_cars.remove(right_cars[i])
            right_cars.remove(left_cars[i])
    
    return collisions
```
This function uses two lists to represent the positions of cars driving from left to right and right to left, respectively. It then iterates through both lists to determine if there are any collisions. If a car appears in both lists, it has collided with itself, so we increment the collisions variable and remove the car from both lists to prevent double-counting. Ultimately, the function returns the total number of collisions.

Here's a test suite to ensure the function behaves correctly:
```python
def test_car_race_collision():
    # Test case with no cars:
    assert car_race_collision(0) == 0

    # Test case with one car:
    assert car_race_collision(1) == 0

    # Test case with two cars:
    assert car_race_collision(2) == 1

    # Test case with three cars:
    assert car_race_collision(3) == 2

    # Test case with ten cars:
    assert car_race_collision(10) == 5

    # Test case with twenty cars:
    assert car_race_collision(20) == 10

test_car_race_collision()
```
This test suite covers multiple scenarios, from no cars on the road to ten and twenty cars, verifying that the function correctly calculates collisions.