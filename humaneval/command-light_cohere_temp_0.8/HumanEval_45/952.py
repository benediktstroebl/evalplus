```python
def triangle_area(a, h):
    return sqrt(a*h + h*h - a*a)

# Test the function
print(triangle_area(5, 3)) # 7.5
print(triangle_area(6, 6)) # 8.0
print(triangle_area(0, 100)) # should fail
```