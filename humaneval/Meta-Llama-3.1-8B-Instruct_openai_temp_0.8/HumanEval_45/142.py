Here's a Python function to calculate the area of a triangle given its base and height, along with a test to verify the function:
```python
def triangle_area(a, h):
    """
    Given length of a side (height in this formula) and height return area for a triangle.
    
    The area of a triangle is calculated by the formula: A = (base * height) / 2
    where 'a' is considered the height for the sake of this function, as height is a reserved keyword in Python.

    Args:
        a (float): The length of the side considered height.
        h (float): The base of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3)) # Expected output: 7.5
print(triangle_area(10, 5)) # Expected output: 25.0
```