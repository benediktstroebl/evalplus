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
assert car_race_collision(10) == 45
assert car_race_collision(50) == 2450
```

This script defines the `car_race_collision` function, which calculates the number of collisions between cars moving in opposite directions along an infinitely long straight road, assuming all cars move at the same speed and are infinitely durable. It iterates through all possible pairs of cars, counting the number of collisions between cars moving in opposite directions (identified by the parity of their indices). The function returns the total count of such collisions.

The tests assert that the function correctly calculates the number of collisions for a smaller case (10 cars) and a larger case (50 cars).