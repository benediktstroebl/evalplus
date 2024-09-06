Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    collisions = 0
    for i in range(n):
        for j in range(n):
            if i != j and (i + j) % 2 == 0:
                collisions += 1
    return collisions

# Tests
assert car_race_collision(1) == 0
assert car_race_collision(2) == 0
assert car_race_collision(3) == 0
assert car_race_collision(4) == 2
assert car_race_collision(100) == 50
```
This script defines the `car_race_collision` function, which calculates the number of collisions between cars moving in opposite directions on an infinitely long straight road. It uses nested loops to iterate through all possible pairs of cars, accounting for the fact that there are `n` cars driving in each direction. The function counts the number of collisions and returns the result. Then, the script includes a few tests to validate the function's behavior for different input values.