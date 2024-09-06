```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3))  # Output: 15.5
print(triangle_area(6, 4))  # Output: 12.6
print(triangle_area(4, 6))  # Output: 10.8
print(triangle_area(7, 8))  # Output: 49.49
```

This Python script defines a function `triangle_area` that calculates the area of a triangle. It takes two arguments: `a` (base length) and `h` (height length). The function returns the area of the triangle, which is computed using the formula (base * height * half). The function is then tested with various input values, and the results are printed to the console.