```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The formula used here is (base * height) / 2. 
    Here base is the side of the triangle and height is given.

    Args:
        a (float): The side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

In this script, the function `triangle_area` takes two parameters: `a` (the side) and `h` (the height). It calculates and returns the area of the triangle using the formula (base * height) / 2. The test case at the end demonstrates how to use the function with a sample input.