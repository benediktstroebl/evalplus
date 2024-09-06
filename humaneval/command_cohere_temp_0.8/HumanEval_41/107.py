Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    num_collisions = 0
    for i in range(n):
        for j in range(n):
            if i != j and (i + j) % 2 == 0:
                num_collisions += 1
    return num_collisions

# Test cases
print(car_race_collision(10))
print(car_race_collision(20))
print(car_race_collision(100))
```
This script defines the `car_race_collision` function, which calculates the number of collisions between cars in the specified problem setup and outputs the result. It does this by iterating through all possible pairs of cars and checking if the difference between their indices is divisible by 2 (indicating they're on opposite sides of the track), and if so, it increments the `num_collisions` counter.

The provided test cases help ensure that the function behaves correctly for different values of `n`.