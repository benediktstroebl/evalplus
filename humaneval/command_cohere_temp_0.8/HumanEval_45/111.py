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
    return 0.5 * a * h
```

This function calculates the area of a triangle using the formula `0.5 * a * h1`, where `a` is the length of the side and `h` is the height or length of the triangle. It successfully returns the area for the given inputs Side length: 5, Height: 3  as testified by the example: `>> triangle_area(5, 3) 7.5` 

To see how to use this function in practice, you can add test cases to ensure that the function calculates the triangle area correctly for a variety of side lengths and heights. Here's an example:
```python
def test_triangle_area():
    # Test case for right triangle with side=5, height=3
    assert triangle_area(5, 3) == 7.5

    # Test case for isosceles triangle with base=6, height=4
    assert triangle_area(6, 4) == 12.0

    # Test case for right triangle with side=10, height=5
    assert triangle_area(10, 5) == 50.0

    # Test case for triangle with side=7, height=9
    assert triangle_area(7, 9) == 63.0
``` 

This way, you can ensure that the function works correctly.  You can add more test cases to cover a variety of triangle configurations and validate the function's correctness.