```markdown
# Calculating Triangle Area
================================

This script calculates the area of a triangle given the length of a side and the height.

### Code
```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
    a (float): The length of the side of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

### Explanation
The area `A` of a triangle is given by the formula `A = 0.5 * base * height`. In this script, `a` is the length of the side of the triangle, which acts as the base, and `h` is the height of the triangle. The function `triangle_area(a, h)` calculates the area using this formula and returns the result. 

### Usage
To use this function, simply call it with the length of the side and the height as arguments, like this: `triangle_area(5, 3)`. The function will return the calculated area.