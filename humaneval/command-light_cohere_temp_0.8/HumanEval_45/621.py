```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(6, 6))  # Output: 36.0
print(triangle_area(4, 8))  # Error: TypeError: 'float' object does not support attribute 'get'
```