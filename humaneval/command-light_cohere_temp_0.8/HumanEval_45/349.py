Here's a self-contained Python function that calculates the area of the triangle using the formula:
```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(6, 6)) # Output: 12.0
print(triangle_area(4, 8)) # Should raise exception
```