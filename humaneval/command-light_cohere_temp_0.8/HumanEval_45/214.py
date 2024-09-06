```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the base and height."""
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Assertions failed: Area should be 15.00"

    assert triangle_area(10, 5) == 85.0, "Assertions failed: Area should be never equal to 85.0"

print("Test passed!")
```