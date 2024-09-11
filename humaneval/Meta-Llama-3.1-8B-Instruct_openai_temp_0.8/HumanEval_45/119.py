```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): The base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base (`a`) and height (`h`). The area is calculated using the formula `0.5 * base * height`. The script then tests this function by calling it with `a = 5` and `h = 3`, and prints the result.