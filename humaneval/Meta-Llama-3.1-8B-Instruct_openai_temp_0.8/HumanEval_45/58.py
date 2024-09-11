### Triangle Area Calculator
#### Problem Description
Calculate the area of a triangle given the length of a side and the height of the triangle.

#### Solution
```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): Length of a side of the triangle
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```
In this solution, we define a function `triangle_area` that takes two parameters, `a` and `h`, which represent the length of a side and the height of the triangle, respectively. The function returns the area of the triangle using the formula `0.5 * base * height`. We then test the function with a sample case.