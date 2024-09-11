### Calculating the Area of a Triangle
### ======================================

Below is a Python function that calculates the area of a triangle given the length of its base (`a`) and its height (`h`).

```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))
```

This function uses the formula for the area of a triangle, which is `(base * height) / 2`. The function takes in two arguments, `a` and `h`, representing the base and height of the triangle respectively. It then returns the calculated area. The example usage at the end shows how to use this function with sample inputs.