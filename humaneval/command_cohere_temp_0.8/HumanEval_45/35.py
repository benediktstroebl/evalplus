```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if h <= 0 or a <= 0:
        raise ValueError("Height and length of side must be positive")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or length of the triangle's legs. This formula is used to calculate the area of a triangle when you know the length of a side and the height.

This code then tests this function:
```python
def test_triangle_area():
    """Tests for the triangle_area function."""
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 10) == 50
    assert triangle_area(0, 1) == 0.5
    assert triangle_area(-1, 2) == -0.5
    assert triangle_area(3, -4) == -6
```

The test_triangle_area function tests the triangle_area function with different inputs, asserting that the area calculated matches the expected value for each scenario.