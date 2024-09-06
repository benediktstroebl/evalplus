Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n: int):
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
assert car_race_collision(10) == 5
assert car_race_collision(100) == 49
```
This code defines a function 'car_race_collision(n)' that simulates a collision between two sets of n cars moving in opposite directions on an infinitely long straight road. It calculates the number of collisions between the cars. 

The function iterates through all possible pairs of cars, checking if the difference between the indices 'i' and 'j' is equal to an even number, indicating that the cars are moving in opposite directions. If so, it increments the 'collisions' count by 1.

Test cases are provided to validate the function's behavior for different values of 'n'. The assert statements compare the expected number of collisions with the output of the 'car_race_collision' function.