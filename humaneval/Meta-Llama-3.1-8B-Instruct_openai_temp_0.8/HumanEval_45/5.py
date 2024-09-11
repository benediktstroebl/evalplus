### Triangle Area Calculation
#### Description
This script defines a function `triangle_area` to calculate the area of a triangle given the length of a side and the height.

#### Code
```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Args:
        a (float): Length of a side.
        h (float): Height of the triangle.
    
    Returns:
        float: Area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
```
#### Note
The area of a triangle is calculated using the formula `A = 0.5 * base * height`. In this code, we assume the length of the side as the base.