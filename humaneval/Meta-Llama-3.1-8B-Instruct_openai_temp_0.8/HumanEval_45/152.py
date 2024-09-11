```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high (height) return area for a triangle.

    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

In this script, the `triangle_area` function takes in two arguments `a` (base) and `h` (height), and returns the area of the triangle using the formula `0.5 * base * height`. The example usage at the end demonstrates how to use the function to calculate the area of a triangle with a base of 5 and a height of 3.