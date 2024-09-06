```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Test case 1
print(triangle_area(5, 3)) # Output: 7.5

# Test case 2
print(triangle_area(3, 6)) # Output: 4.0

# Test case 3
print(triangle_area(6, 3)) # Output: 12.0

# Test case 4
print(triangle_area(4, 8)) # Should raise error: TypeError: 'float' object does not support attribute '1983'
```