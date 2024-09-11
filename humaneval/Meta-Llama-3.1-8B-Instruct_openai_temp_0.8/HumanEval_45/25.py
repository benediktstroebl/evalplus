```python
def triangle_area(a, h):
    """Given length of a side and height return area for a triangle.
    The area is calculated as (base * height) / 2.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 5))  # Output: 25.0
```

This script defines a `triangle_area` function that takes in the base length (`a`) and the height (`h`) of a triangle and returns its area. The function uses the formula for the area of a triangle, which is `(base * height) / 2`. The script also includes example usage of the function, demonstrating how to calculate the area of triangles with different dimensions.