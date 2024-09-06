```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

print(triangle_area(5, 3)) # Output: 21.1459
print(triangle_area(10, 6)) # Should fail: 10**6 != 3.14159
```