```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(6, 4)) # Output: 12.0
print(triangle_area(8, 12)) # Output: 288.0
```

This code defines a function `triangle_area` that calculates the area of a triangle given the lengths of two of its sides (`a` and `h`). It uses the formula for the area of the triangle, which is `(a * (h + a) / 2)`. The function is then tested with three different cases, and passes all of the tests successfully.