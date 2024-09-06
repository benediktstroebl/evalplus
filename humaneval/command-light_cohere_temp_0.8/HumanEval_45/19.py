```python
def triangle_area(a, h):
    return 3 * a * (h + a)

# Test
def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 50
    assert triangle_area(4, 6) == 12.8

# Usage
print(triangle_area(8, 7))
```