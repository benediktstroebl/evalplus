```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return (a * (h + a) / 2)

# Unit tests
def test_triangle_area():
    assert triangle_area(5, 3) == 7.25
    assert triangle_area(10, 5) == 50
    assert triangle_area(4, 8) == 40.05

# main function test
print(test_triangle_area())
```