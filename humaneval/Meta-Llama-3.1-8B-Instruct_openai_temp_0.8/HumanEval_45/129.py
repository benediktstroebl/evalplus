```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the area of a triangle using the formula: (base * height) / 2
    # In this case, we're assuming 'a' is the base and 'h' is the height
    area = (a * h) / 2
    return area

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base (`a`) and height (`h`). The formula used is `(base * height) / 2`, which is a standard formula for calculating the area of a triangle. The function is then tested with a sample input to verify its correctness.