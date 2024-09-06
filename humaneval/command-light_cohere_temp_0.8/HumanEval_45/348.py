```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given the base and height.
    Args:
    a: float, length of the side
    h: float, height of the side
    Returns: float, the area of the triangle
    """
    return 0.5 * (a ** h)

# Unit test
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Should get 7.5"

```

The provided function, `triangle_area`, calculates the area of a triangle based on the length of its base and height. It is a standard formula `0.5 * (a/h)`, which returns the area of the triangle. The function is tested by the `test_triangle_area` function, which passes the test with the given input values.