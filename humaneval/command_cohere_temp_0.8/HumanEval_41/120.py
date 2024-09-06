Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    return max(0, cars_left - cars_right)

# Tests:
test_collisions = [
    (0, 0),
    (1, 0),
    (2, 0),
    (4, 2),
    (10, 5),
    (16, 7),
    (100, 45),
]

for expected, n in test_collisions:
    assert car_race_collision(n) == expected
```

In this implementation, the idea is to balance the number of cars between the two sides. Since there're n cars in total, we have `cars_left` be the number of cars driving left (half of n) and `cars_right` be the number of cars driving right (the other half of n).

We then return the absolute difference between `cars_left` and `cars_right` as the maximum possible number of collisions. This is because the cars in the two halves only collide with each other, and the number of collisions is maximized when the number of cars in the two halves are equal (i.e., one side has n- number of cars, so the difference is at its maximum).

The unit tests are also provided to validate the function against a variety of inputs. You can modify the `test_collisions` list to test further scenarios and ensure the function operates as expected. Feel free to experiment and test with other inputs, and let me know if you'd like to discuss further or tackle another problem!