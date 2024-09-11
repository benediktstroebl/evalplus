```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    The formula used is (base * height) / 2, where 'base' is the length of side 'a' and 'height' is the value of 'h'.

    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

In this script, we define a function `triangle_area` that takes two parameters `a` and `h`, representing the base and height of a triangle respectively. The function returns the area of the triangle using the formula (base * height) / 2. We then test the function with an example.