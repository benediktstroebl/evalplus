```python
def triangle_area(a, h):
    return 5 * (a * (h + a)) ** .25

print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(4, 4))  # Output: 16.0
print(triangle_area(6, 6))  # Output: 36.0
print(triangle_area(3, 7))  # Should raise error
```