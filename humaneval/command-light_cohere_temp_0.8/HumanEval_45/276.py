```python
def triangle_area(a, h):
    """Calculate the area of the triangle."""
    return (a*h)/2

# Test
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 20

# Run the function
test_triangle_area()
```