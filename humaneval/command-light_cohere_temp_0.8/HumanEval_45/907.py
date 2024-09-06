```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3)) # prints (5* (3+5) / 2)^(1/2) = 35.0
print(triangle_area(6, 4)) # prints (6* (4+6) / 2)^(1/2) = 52.0
print(triangle_area(8, 8)) # prints (8* (8+8) / 2)^(1/2) = 64.0
```