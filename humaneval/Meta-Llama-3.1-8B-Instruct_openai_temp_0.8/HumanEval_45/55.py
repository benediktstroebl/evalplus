### Calculating Triangle Area
#### Python Script

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): Length of the side of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
if __name__ == "__main__":
    print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two parameters: `a` (length of the side of the triangle) and `h` (height of the triangle). The function returns the area of the triangle using the formula `0.5 * base * height`. The example usage at the end demonstrates how to call the function with specific values.