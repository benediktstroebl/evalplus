```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function takes in three numbers representing the lengths of the sides of a triangle. Using the fact that the semi-perimeter s of a triangle satisfies the inequality `s >= max(a, b, c)` for the three sides a, b, and c, the function first checks if the given sides form a valid triangle. If the inequality is satisfied, the function calculates the area of the triangle using the formula for the area of a triangle from its semi-perimeter, and rounds the result to two decimal places. If the given sides do not form a valid triangle, the function returns -1.

Here is a test suite that could be used to validate the function:
```python
def test_triangle_area():
    # Valid triangle
    assert triangle_area(3, 4, 5) == 6.00

    # Invalid triangle
    assert triangle_area(1, 2, 10) == -1

    # Another valid triangle
    assert triangle_area(5, 12, 13) == 30.86

    # Edge case: one side is the sum of the other two
    assert triangle_area(10, 5, 0) == -1
```

The test suite contains several test cases, including valid and invalid triangles, to validate the function performs as expected.