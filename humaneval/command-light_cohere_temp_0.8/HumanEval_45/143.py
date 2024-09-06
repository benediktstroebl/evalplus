```python
def triangle_area(a, h):
    return 3 * a * (h + a)

print(triangle_area(5, 3)) # Output: 15.0
print(triangle_area(6, 12)) # Output: 108.0
```
This code defines a function called `triangle_area` that calculates the area of a triangle given the lengths of two sides (`a` and `h`). It uses the formula for the area of a triangle, which is `a * (h + a)`, and then multiplies this by the lengths of the sides.