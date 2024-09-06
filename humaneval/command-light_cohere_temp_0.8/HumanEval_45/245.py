```python
def triangle_area(a, h):
    """
    Calculate the area of the triangle.
    Parameters:
    a (length of the triangle's side)
    h (height of the triangle's side)
    Returns:
    The area of the triangle
    """
    return (a * h) ** .5

# Unit tests
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 2) == 12.8
    assert triangle_area(8, 4) == 35.6

print('Test suite passed!')
```