```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # prints: 15.0
print(triangle_area(5, 4)) # prints: 20.0
print(triangle_area(6, 8)) # prints: 60.0
print(triangle_area(10, 10)) # fails
```