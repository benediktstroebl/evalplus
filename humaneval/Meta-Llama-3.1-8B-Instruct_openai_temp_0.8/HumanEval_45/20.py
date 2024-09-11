```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Parameters:
    a (float): Length of the side of the triangle.
    h (float): Height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Testing the function
print(triangle_area(5, 3))  # Output: 7.5
```

In this code, the `triangle_area` function takes two arguments, `a` and `h`, which represent the length of a side and the height of the triangle respectively. It uses the formula `0.5 * base * height` to calculate the area of the triangle. The function includes a docstring that describes its purpose, parameters, and return value. The example usage is documented using doctests. Finally, the code includes a test call to the function to demonstrate its usage.