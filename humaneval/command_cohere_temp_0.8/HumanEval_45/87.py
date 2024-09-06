```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can call it with the length of a side and the height of the triangle, and it will return the area of the triangle. Test cases can be added to ensure the function correctness. Here is an example of adding a test: 
 ```python
import pytest

def test_triangle_area():
    # Test case one
    a = 5
    h = 3
    expected = 7.5
    result = triangle_area(a, h)
    assert result == expected
```