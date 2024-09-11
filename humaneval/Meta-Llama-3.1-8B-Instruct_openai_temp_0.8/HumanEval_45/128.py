### Triangle Area Calculator
#### Problem Statement

Given the length of a side and the height of a triangle, return the area of the triangle.

#### Solution
```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): The length of the side.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    # The area of a triangle is calculated as (base * height) / 2
    area = (a * h) / 2
    return area
```
#### Example Usage
```python
# Calculate the area of a triangle with side length 5 and height 3
print(triangle_area(5, 3))  # Output: 7.5

# Calculate the area of a triangle with side length 10 and height 2
print(triangle_area(10, 2))  # Output: 10.0
```