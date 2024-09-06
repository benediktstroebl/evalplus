```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3)) # prints: 15.0
print(triangle_area(10, 5)) # prints: 50.0
print(triangle_area(8, 6)) # should raise error
```