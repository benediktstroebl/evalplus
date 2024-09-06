```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * a * h
```

The function `triangle_area` accepts the length of a side `a` and the height `h` of the triangle as arguments and calculates its area using the formula `0.5 * a * h`. It then returns the calculated area. 

To ensure accuracy, the function does not rely on any external variables and is self-contained, making it easy to reuse and incorporate into other projects without worrying about compatibility issues. 

You can verify the function's correctness by calling it with specific side length and height values and comparing the results with the expected output.