```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given the base and height.
    Args:
        a, base of triangle 
        h, height of triangle
    Returns: 
        float: The area of the triangle
    """
    return 0.5*a*h  # This is a placeholder for the formula

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test"
```