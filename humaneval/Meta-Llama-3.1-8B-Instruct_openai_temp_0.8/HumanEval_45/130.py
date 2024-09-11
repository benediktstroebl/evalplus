### Triangle Area Calculator
#### Script Description

This Python script calculates the area of a triangle given its base length and height.

#### Code
```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high return area for a triangle.
    
    Args:
        a (float): Base length of the triangle.
        h (float): Height of the triangle.
        
    Returns:
        float: Area of the triangle.
    
    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```
#### Explanation

This script defines a function `triangle_area` that takes two arguments `a` (base length) and `h` (height), calculates the area using the formula `0.5 * base * height`, and returns the result. The example usage demonstrates how to call the function and print the result.