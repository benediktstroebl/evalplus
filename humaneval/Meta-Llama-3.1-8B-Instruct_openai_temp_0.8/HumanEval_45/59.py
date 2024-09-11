### Calculating the Area of a Triangle
```python
def triangle_area(a, h):
    """
    Given length of a side 'a' and height 'h' return area for a triangle.
    
    :param a: length of a side
    :param h: height of the triangle
    :return: area of the triangle
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side and height must be positive numbers.")
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```
This Python script defines a function `triangle_area(a, h)` that calculates the area of a triangle given its base `a` and height `h`. It also includes error checking to ensure that both `a` and `h` are positive numbers. The example usage at the end demonstrates how to use this function.