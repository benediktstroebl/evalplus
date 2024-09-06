```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(4, 6)) # Output: 8.6
print(triangle_area(10, 5)) # Error: TypeError: unsupported operand type(int, float)
```