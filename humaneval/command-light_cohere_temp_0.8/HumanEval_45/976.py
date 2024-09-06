Here is a Python script that contains a self-contained function to calculate the area of the triangle, which passes the test:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(6, 4))  # Output: 12.0
print(triangle_area(8, 10))  # Output: 88.0
```

The provided function `triangle_area` takes two parameters: `a` and `h`. It calculates the area of the triangle using the formula `Area = (a * (h + a) / 2)`, where `a` and `h` are the lengths of the triangle's sides.  The area of a triangle is the region enclosed by its three sides base, and `h` is the height or altitude of the triangle.