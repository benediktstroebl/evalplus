```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * a * h
```

To ensure the robustness of the function, test cases should be added to cover different scenarios and corner cases. Here are some additional tests that can be added:
```python
# Test case with all positive values
assert triangle_area(3, 4) == 6.0

# Test case with side length as zero
assert triangle_area(0, 5) == 0.0

# Test case with side length and height equal to the same value
assert triangle_area(5, 5) == 12.5

# Test case with negative values
assert triangle_area(-2, 3) == -3.0
```

This way, the function is guaranteed to work seamlessly across different scenarios, producing the expected results.