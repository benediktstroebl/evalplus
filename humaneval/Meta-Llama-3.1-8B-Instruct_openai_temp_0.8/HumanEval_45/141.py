### Triangle Area Calculator
#### Python Script
```markdown
```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    The area of a triangle is calculated using the formula: area = 0.5 * base * height
    
    Args:
        a (float): Length of a side
        h (float): Height of the triangle
        
    Returns:
        float: Area of the triangle
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```
```