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
        raise ValueError("Height and length of side must be positive")
    
    return 0.5 * a * h
```

The function prompts users to input the length of a side and height of a triangle, then returns the area of the triangle based on these measurements. It also includes input validation to ensure that the inputs are positive numbers, throwing a `ValueError` if they're not.

To use this function, you can call it with specific measurements and it will return the area of the corresponding triangle:
```python
area = triangle_area(5, 3)
print(area)  # This will output: 7.5
``` 
If you wish to have the unit of the area (e.g., square units) returned as well, we can easily modify the function to include that. Let me know if you'd like to see that change or if you have any other questions at all!