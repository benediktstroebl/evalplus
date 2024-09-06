```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3)) # prints expected output: 15.0
print(triangle_area(5, 4)) # throws error: TypeError: unsupported operand type(int, float)
```