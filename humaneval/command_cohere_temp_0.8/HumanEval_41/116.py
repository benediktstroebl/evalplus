Here's a Python script that contains a function which solves the car collision problem as per the provided markdown code block:
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

# Tests
assert car_race_collision(5) == 0
assert car_race_collision(6) == 0
assert car_race_collision(7) == 1
assert car_race_collision(10) == 5
```

This code defines the `car_race_collision` function, which takes in the number of cars `n` as input. It calculates the number of "cars left" and "cars right" based on half of `n` and then uses nested loops to determine if any of the left-moving cars intersect with the right-moving cars. If the sum of the indices of the left-moving car and the right-moving car is greater than or equal to the total number of cars `n`, it means they have collided, and `collisions` is incremented. The function returns the total count of collisions.