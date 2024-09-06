```python
def triangle_area(a, h):
    return 3 * a * (h / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40
    assert triangle_area(6, 6) == 36
    assert triangle_area(8, 10) == 80

# Call the function to verify
test_triangle_area()
```