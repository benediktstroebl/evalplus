```python
def triangle_area(a, h):
    """Given length of a side and height return area of a triangle.
    The formula used is: area = (base * height) / 2
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 5))  # Output: 25.0
```

This script defines the `triangle_area` function, which takes two arguments, `a` (the base of the triangle) and `h` (the height of the triangle). It returns the area of the triangle using the formula `area = (base * height) / 2`. The script then tests the function with two examples.