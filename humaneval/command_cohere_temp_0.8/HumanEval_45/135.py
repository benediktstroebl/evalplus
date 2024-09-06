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

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or length of the triangle's legs. This formula is used to calculate the area securely. This function also includes inputs and outputs (I/O) tests. 
If you want to test more cases to ensure the function is working properly, you can add more tests. Here's an example:
```python
# Test case for the triangle_area function
def test_triangle_area():
    # Test case where both sides are the same
    assert triangle_area(5, 3) == 7.5 
    # Test case with sides < 0
    assert triangle_area(-5, 3) == 0.5 
    # Test case with sides = 0
    assert triangle_area(0, 0) == 0 
    # Test case with negative height and positive length
    assert triangle_area(5, -3) == -1.5 
    # Test case with invalid inputs
    assert triangle_area(5, '3') == 'a' != float
```

In the above code, a test case is added for each feature of the function to ensure that the function is working as expected. 

If you encounter any errors or have any doubts about the working of the function, let me know and I'll be happy to help!