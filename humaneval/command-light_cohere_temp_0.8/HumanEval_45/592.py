```python
def triangle_area(a, h):
    return 3.14 * a *a * (a ** 2 + h ** 2) ** 0.25

print(triangle_area(5, 3))  # Should return 7.0
print(triangle_area(10, 6))  # Should return 163.0
```