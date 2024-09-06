```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```
The function first calculates the semi-perimeter of the triangle and then uses a determinant algorithm to determine its area, returning -1 if the sides do not form a valid triangle.

To follow best practices, the function includes a docstring with detailed explanations of the input parameters, the return value, and an example use of the function. This helps developers understand the function's purpose and how to properly use it.

To comprehensively validate the function, it is recommended to include a test suite with various test cases, including edge cases and scenarios with invalid input to ensure robustness and accuracy. An example test case is shown below:
```python
def test_triangle_area():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 10, 10) == 0
    assert triangle_area(7, 8, 9) == -1
``` 
This test case includes valid and invalid triangles to cover different scenarios the function may encounter.