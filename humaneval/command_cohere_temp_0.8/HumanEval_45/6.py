```python
def triangle_area(a, h):
    """
    Calculates the area of a triangle given the length of a side and its height.
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
# Test case with all sides equal
assert triangle_area(5, 5) == 12.5

# Test case with a = 0 (degenerate case)
assert triangle_area(0, 1) == 0

# Test case with h = 0 (degenerate case)
assert triangle_area(1, 0) == 0

# Test case where a is negative
assert triangle_area(-2, 3) == -3
```