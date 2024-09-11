## Calculating Triangle Area
### Problem Statement
Calculate the area of a triangle given the length of a side and the height.

### Solution
```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): The length of the base (side) of the triangle.
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
This script defines a function `triangle_area` that takes in two parameters: `a` (the length of the base) and `h` (the height of the triangle). It calculates the area of the triangle using the formula `0.5 * base * height` and returns the result. The example usage is provided to demonstrate the function's usage.