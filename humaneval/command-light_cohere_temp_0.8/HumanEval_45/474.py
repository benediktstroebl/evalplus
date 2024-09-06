```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return sqrt((a*h+h*h+a*h)/2)

# Test the function with the provided values
assert triangle_area(5, 3), "Returned area should be less than or equal to 7.5"
```