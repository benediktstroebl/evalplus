```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * a * h
```
In the above code, the function `triangle_area` calculates the area of a triangle using the formula `Area = 0.5 * a * h`, where `a` is the length of a side and `h` is the height. This formula is based on the principle that the area of a triangle is equal to half of the product of its base and height. 

You can ensure the function works as expected by testing it with different inputs:
```python
>>> triangle_area(5, 3)
7.5
>>> triangle_area(7, 10)
35
```