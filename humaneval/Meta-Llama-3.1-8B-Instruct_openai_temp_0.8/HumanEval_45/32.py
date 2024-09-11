```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): length of a side of the triangle
        h (float): height of the triangle

    Returns:
        float: area of the triangle
    """
    return 0.5 * a * h

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
```

In this script, the `triangle_area` function takes in two parameters, `a` and `h`, which represent the length of a side and the height of the triangle, respectively. It returns the area of the triangle using the formula `0.5 * base * height`. The script includes a docstring with a description of the function, its arguments, and its return value, following professional guidelines for code documentation. The example usage at the end demonstrates how to call the function and print the result.