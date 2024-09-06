```python
def triangle_area(a, h):
    return 5 * (a**2 + h**2) ** .5

print(triangle_area(5, 3))  # Output: 15.5
print(triangle_area(5, 4)) # Should fail with ValueError
```