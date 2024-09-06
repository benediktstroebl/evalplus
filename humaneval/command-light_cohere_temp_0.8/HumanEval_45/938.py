```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

# Test function
def test():
    assert triangle_area(5, 3) == 7.5, "Passed test"
```