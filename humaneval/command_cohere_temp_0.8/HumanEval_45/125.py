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
        raise ValueError("Height and length of side must be positive numbers.") 
    area = 0.5 * a * h 
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of the side and `h` is the height. This formula is used to calculate the area of a triangle when you know the length of a side and the height. The output of this function is the area of the triangle. 

The function includes docstrings that provide information about the purpose of the function, the arguments it takes, what it returns, and an example of how to use it. This should make the code more understandable. 

To run the code ensure you have Python installed. You can run the script in the Python environment with the following command:
```python
python script.py
```

And the script could look like this:
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
        raise ValueError("Height and length of side must be positive numbers.") 
    area = 0.5 * a * h 
    return area

# Tests
a = 5
h = 3
print(triangle_area(a, h))
```

This will run the function with the arguments 5 and 3 and print out the area of the corresponding triangle. Adjusting the values of a and h will change the output accordingly.