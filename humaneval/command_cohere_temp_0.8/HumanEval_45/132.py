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
        raise ValueError("Height and side length must be positive")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or length of the triangle's legs opposing the side of length `a`. This formula is used to calculate the area of triangles with equal lengths and heights.

To ensure that the function only accepts positive values for `a` and `h`, input validation is implemented to check for negative values. If any of the inputs are negative, a `ValueError` is raised. 

This approach ensures the efficiency of the function and makes it more robust against different use cases. 
  
  Output:
  ```
  7.5
  ```

This is a self-contained Python script that solves the problem statement. It includes a function `triangle_area` that takes in two arguments, `a` and `h`, and returns the area of a triangle based on the given side length and height. 

The function also includes a demonstration of the function's usage and a validation that ensures inputs are positive numbers.