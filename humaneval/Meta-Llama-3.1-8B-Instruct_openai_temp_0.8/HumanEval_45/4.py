```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    The formula used to calculate area is: Area = 0.5 * base * height
    
    Parameters:
    a (float): The length of the side of the triangle (base)
    h (float): The height of the triangle
    
    Returns:
    float: The area of the triangle
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
if __name__ == "__main__":
    print(triangle_area(5, 3))
```

In this script, we define a function `triangle_area` that takes two arguments: `a` and `h`, representing the base and height of the triangle respectively. We then return the area using the formula `0.5 * base * height`. The script also includes an example usage of the function at the end.