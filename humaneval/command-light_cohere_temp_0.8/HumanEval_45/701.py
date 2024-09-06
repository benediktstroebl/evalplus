```python
def triangle_area(a, h):
    return sqrt(a*h + h*h - a*a)

# Test the function
print(triangle_area(5, 3)) # 7.5
print(triangle_area(4, 6)) # 16.0
print(triangle_area(6, 4)) # 12.0
print(triangle_area(8, 10)) # 93.0
```