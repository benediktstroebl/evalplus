```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(6, 6)) # Output: 24.0
print(triangle_area(8, 10)) # Error: Exception: cannot multiply without int64
```