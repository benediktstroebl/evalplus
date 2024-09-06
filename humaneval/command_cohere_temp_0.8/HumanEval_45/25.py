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
    if h == 0: 
        return 0  # Divide by zero error if height is 0
    return 0.5 * a * h
    ```

The function incorporates a check for a divide by zero error when the height is zero. 

To ensure clarity and robustness, it's essential to handle edge cases appropriately and provide informative error messages or behavior.