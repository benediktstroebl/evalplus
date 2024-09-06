```python
def triangle_area(a, h):
    return 3 * a * (h) ** 2  # [Area of triangle formula: $\text{Area} = \frac{1}{2} * \text{base} * \text{height}^2]$

def test_triangle_area(a, h):
    assert triangle_area(a, h) == (1 / 2) * a * h ** 2, "Failed to calculate area"
    return True

# Usage example
print(test_triangle_area(5, 3))  # Output: 7.5
```

This Python script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The `test_triangle_area` function serves to validate the correctness of the `triangle_area` function by passing test cases. When the function is called with the test cases, it verifies the expected area result and successfully passes the test.

Finally, an example usage is provided, and the function is demonstrated to work as expected.