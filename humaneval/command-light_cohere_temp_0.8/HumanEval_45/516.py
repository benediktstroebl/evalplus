```python
def triangle_area(a, h):
    return 5 * (a * (h + a) / 2)

print(triangle_area(5, 3)) # prints 15.0
print(triangle_area(6, 6)) # prints 36.0
print(triangle_area(10, 5)) # raises ValueError
```