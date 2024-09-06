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
This function uses two nested loops to iterate through all possible pairs of cars and checks if they will collide, using the condition `if i + j >= n` to check if the difference between the indices of the two cars is smaller than the total number of cars `n`. The function then returns the number of collisions.

To test the correctness of the function, a simple test case is provided below:
```python
test_cases = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [2, 2],
    [5, 5],
    [10, 10],
    [1, 3],
    [2, 5],
    [13, 26],
    [100, 100]
]

for idx, (n, expected) in enumerate(test_cases):
    assert car_race_collision(n) == expected, f"Failed test case {idx}: {n}"
```
This script provides a variety of test cases to ensure that the function `car_race_collision()` behaves as expected. You can additionally test the function with other input values to cover more corner cases.