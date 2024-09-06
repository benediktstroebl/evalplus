```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2)

print(triangle_area(5, 3)) # Output: 45
print(triangle_area(5, -3)) # Should raise an error: ValueError
print(triangle_area(0, 10)) # Should raise an error: TypeError
```