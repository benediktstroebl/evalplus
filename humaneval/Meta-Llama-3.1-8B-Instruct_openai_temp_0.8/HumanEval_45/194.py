```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # The formula to calculate the area of a triangle is: (base * height) / 2
    area = (a * h) / 2
    return area

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side (`a`) and the height (`h`). The area is calculated using the formula `(base * height) / 2`. The script then tests the function with the example input provided in the docstring.