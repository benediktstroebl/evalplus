```python
def triangle_area(a, h):
    """Calculate the area of the triangle."""
    return sqrt((a * (h + a)) / 2)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(10, 5) == 52

# Test case 3
try:
    import(triangle_area)(0, 0)
except Exception as e:
    print(e)
```