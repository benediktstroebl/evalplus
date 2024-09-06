```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test function that checks if triangle_area returns the correct result
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Test failed!"
```