```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if h <= 0 or a <= 0:
        raise ValueError("Height and side length must be positive numbers.") 
    area = 0.5 * a * h 
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of the side and `h` is the height. This formula is used to calculate the area of a triangle when you know the length of a side and the height. The output of the example provided in the docstring is also added to ensure the function behaves as expected. 

To handle invalid inputs, a `ValueError` is raised when `h` is less than or equal to 0 or `a` is less than or equal to 0, ensuring that only valid inputs are provided. 

Please let me know if any additional clarification is needed.