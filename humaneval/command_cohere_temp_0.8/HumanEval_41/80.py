Here's a Python script that contains a function which solves the car collision problem as per the provided markdown code block:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0
    for i in range(cars_left):
        for j in range(cars_right):
            if i != j:
                collisions += 1
    return collisions

# Tests
assert car_race_collision(10) == 2
assert car_race_collision(100) == 50
```
This script includes a function called `car_race_collision(n)` which serves the purpose of calculating the number of collisions out of `n` cars driving left to right and another `n` cars driving right to left on an infinitely long straight road. The function firstly calculates the totals cars driving left and right, respectively, then proceeds to iterate through the cars while checking for potential collisions between the two sets of cars. It counts the number of collisions and subsequently returns this count. The test cases provided are meant to verify the correctness of the function's behavior for different scenarios.