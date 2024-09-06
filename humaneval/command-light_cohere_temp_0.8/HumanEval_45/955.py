```python
def triangle_area(a, h):
    return max(0, a * (h + 1) / 2)

print(triangle_area(5, 3))  # Should return 7.5
print(triangle_area(10, 3))  # Should return 23.0
print(triangle_area(0, 5))  # Should return 0
print(triangle_area(-10, 3))  # Should raise exception
```