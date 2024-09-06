```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(a, b, c) * (s - max(a, b, c)) / 2)
        return round(area, 2)
    else:
        return -1
```

The function follows the logic you provided in the original prompt. It first checks whether the sum of the sides is equal to the longest side to determine whether it is a valid triangle. If the condition is met, it calculates the area and rounds it to two decimal places, as per the prompt instructions. Otherwise, it returns -1. 

To see how the function performs against specific test cases, you can run the following code:
```python
test_cases = [
    (3, 4, 5, 6.00),
    (1, 2, 10, -1),
    (10, 100, 1010, 2541.00),
    (7, 8, 9, -1),
]

for a, b, c, expected in test_cases:
    actual = triangle_area(a, b, c)
    assert actual == expected
```

This block of code provides a set of test cases to validate the `triangle_area` function. Each test case is a tuple comprising the side lengths and the expected area or `-1` for invalid triangles. The `assert` statement checks whether the actual result matches the expected value for each test case.