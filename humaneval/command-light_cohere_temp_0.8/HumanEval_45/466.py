```python
def triangle_area(a, h):
    return max(3.0 * (a + h) for a in [1, 5, 10])

print(triangle_area(5, 3))  # Should print 15.0
print(triangle_area(10, 3))  # Should print 30.0
```