Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0
    for i in range(cars_left):
        for j in range(cars_right):
            if i + j >= n:
                collisions += 1
    return collisions
```
This function uses two nested loops to account for all possible collisions between the cars travelling in opposite directions. It calculates the number of collisions by incrementing the `collisions` variable each time the inner loop iterates without accounting for the cars that have already collided. 

To test this function, you can use the following code:
```python
test_collisions = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 5),
    (6, 6),
    (7, 0),
    (8, 2),
    (9, 0),
    (10, 4)
]
for expected, test in test_collisions:
    assert car_race_collision(test) == expected
```
This provides a test suite to validate the correctness of the solution against expected outputs.