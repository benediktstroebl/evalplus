### Triangle Area Calculator
#### Python Script

```python
def triangle_area(a, h):
    """
    Given length of a side and height (in the case of an isosceles triangle)
    return area for a triangle.

    The formula used is: area = (base * height) / 2

    Args:
        a (float): Length of a side
        h (float): Height of the triangle

    Returns:
        float: Area of the triangle
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given its base (`a`) and height (`h`). It uses the formula `area = (base * height) / 2` and returns the calculated area. The example usage at the end demonstrates how to call the function with specific values and print the result.