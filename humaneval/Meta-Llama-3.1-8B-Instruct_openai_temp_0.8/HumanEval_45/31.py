The formula to calculate the area of a triangle is 0.5 * base * height, where base is the length of a side and height is the height of the triangle. We will implement this formula in a Python function.

```markdown
### Triangle Area Calculator

This script provides a function `triangle_area` to calculate the area of a triangle given its length of a side and height.
```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): Length of a side.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two arguments, `a` and `h`, representing the length of a side and the height of the triangle respectively. It calculates and returns the area of the triangle using the formula `0.5 * a * h`. The script also includes a test case to demonstrate how to use the function.