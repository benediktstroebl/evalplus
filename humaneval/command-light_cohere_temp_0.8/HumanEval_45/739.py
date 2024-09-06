```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the lengths of two sides.
    Args:
    a (the length of the base)
    h (the length of the height)
    Returns: 
    The area of the triangle.
    """
    # Implement the area formula: base * height / 2
    # Calculate area
    area = (a * h) / 2
    return area

# Unit tests
assert triangle_area(5, 3) == 7.5
assert triangle_area(8, 6) == 28.25
assert triangle_area(10, 5) == 50

``` 
The provided code calculates the area of a triangle based on the given base and height. It uses the area formula and stores it in the 'triangle_area' function. The unit tests are also added to ensure the function works correctly.