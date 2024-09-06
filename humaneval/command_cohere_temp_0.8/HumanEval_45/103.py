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
    if h == 0: 
        return 0  # Divide by zero error if height is 0
    area = (a * h) / 2  # Triangle area equation (base * height) / 2
    return area
```

To ensure that the function handles potential errors, the script checks for a `divide by zero` error if the height is 0. 

To ensure the correctness of the function, it passes the following test:
```python
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
```