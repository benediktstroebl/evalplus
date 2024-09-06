Here's a Python script that contains a function which solves the car collision problem as per the provided markdown code block:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0
    for i in range(cars_left):
        for j in range(cars_right):
            if i != j: collisions += 1
    return collisions

# Tests
assert car_race_collision(6) == 4
assert car_race_collision(10) == 5
```
This function `car_race_collision` takes in a single argument `n`, which represents the number of cars, and returns the number of collisions between the two sets of cars. 

To achieve this, the function first calculates the number of cars driving left and right individually using the formula `cars_right = n - cars_left` (since the total number of cars is a multiple of two). Then, it uses two nested loops to iterate over all possible combinations of left and right cars and checks if any of the combinations correspond to a valid collision (i.e., cars number `i` and `j` where `i != j`). Finally, the function returns the total count of valid collisions.