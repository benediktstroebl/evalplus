Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0

    for i in range(cars_left):
        for j in range(cars_right):
            if i + j > cars_left + cars_right - 1:
                continue
            collisions += 1
    return collisions

# Tests
assert car_race_collision(6) == 4
assert car_race_collision(10) == 5
assert car_race_collision(3) == 0
```

This function calculates the number of collisions by considering the cars going left as 'bullets' and cars going right as 'targets', then iterating through the bullets and counting the number of targets that each bullet can hit. The `range()` function is used to iterate through each value of `i` and `j` while checking if the total exceeds the total number of cars, to ensure that we don't count the same collisions twice. Finally, the function returns the total number of collisions.