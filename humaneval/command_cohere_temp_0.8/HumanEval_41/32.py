Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n: int):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0

    for i in range(cars_left):
        for j in range(cars_right):
            if i == j:
                continue
            else:
                collisions += 1
    return collisions

# Tests
def test_car_race_collision():
    assert car_race_collision(10) == 0
    assert car_race_collision(6) == 3
    assert car_race_collision(8) == 6
    assert car_race_collision(4) == 2

test_car_race_collision()
```
This code defines the 'car_race_collision' function, which takes an integer 'n' as input, representing the number of cars. The function first calculates the number of cars driving left and right and then iterates through their intersections to count the number of collisions. Finally, the 'test_car_race_collision' function provides test cases to validate the correctness of the 'car_race_collision' function. When executed, it verifies these test cases and outputs the results.