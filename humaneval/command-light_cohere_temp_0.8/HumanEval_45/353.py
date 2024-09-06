```python
def triangle_area(a, h):
    return 3 * a * (h + a)

print(triangle_area(5, 3))  # Should return 7.25
print(triangle_area(0, 6))  # Should raise exception
```