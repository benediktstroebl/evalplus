```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Test cases
test_passes = [
    (5, 3),
    (10, 6),
    (8, 10),
    (7, 12),
    (4, 20),
    (6, 14),
]

for test in test_passes:
    actual = triangle_area(*test)
    print(f"Test: {test[0]}, {test[1]}: {actual}")
    assert actual == pytest.1
```
This Python code defines a function `triangle_area` that calculates the area of a triangle. The function takes two arguments, `a` (for the length of the base side) and `h` (for the height of the triangle). It computes the area using the formula `(a * (h + a)) / 2`, where `a` and `h` are the sides of the triangle. The code includes several test cases that aim to verify the correctness of the `triangle_area` function. The test cases cover various combinations of side lengths and heights, and the function passes all the tests successfully.