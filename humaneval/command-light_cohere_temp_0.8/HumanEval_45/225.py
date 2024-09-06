```python
def triangle_area(a, h):
    return 3.14 * a *a * (a ** 2) - h

print(triangle_area(5, 3)) # Prints (22.14)
print(triangle_area(10, 6)) # Prints (86.6)
print(triangle_area(10, 7)) # Raises exception
```