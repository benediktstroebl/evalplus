```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): Length of one side of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

In this script, the function `triangle_area` calculates the area of a triangle given the length of one side (`a`) and its height (`h`). The formula used is `A = 0.5 * base * height`. The area is then returned by the function. The example usage at the end shows how to use the function to calculate the area of a triangle with side length 5 and height 3.