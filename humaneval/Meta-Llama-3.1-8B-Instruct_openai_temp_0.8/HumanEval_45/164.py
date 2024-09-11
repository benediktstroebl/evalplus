```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the area of the triangle using the formula: area = 0.5 * base * height
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two arguments, `a` and `h`, representing the base and height of the triangle, respectively. It calculates and returns the area of the triangle using the formula `area = 0.5 * base * height`. The script then tests the function with sample input and prints the result.