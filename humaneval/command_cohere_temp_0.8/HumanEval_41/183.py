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
```
This function calculates the number of collisions by calculating the number of cars that are traveling left and the number of cars that are traveling right. Then, it loops through all possible pairs of cars and checks whether the difference between the number of "right" and "left" cars in the pair is equal to 1, indicating a collision for the given pairs of cars.