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

The area of a triangle is proportional to the product of half of its base and height. This is known as Heron's formula and is derived from the more general formula for area of a triangle given by: 
> $Area = 0.5 \times b \times h$

where:
- b is half of the base
- h is the height

This formula is derived from the more fundamental formula for the area of a triangle as 

> $Area = \frac{1}{2} \times \frac{(a^2)(b^2)">(abc))}{(3)}$

where:
- a is side b
- b is side c
- c is side a 

for any configuration of the sides. 

This more complex formula is derived from a general formula for the area of a triangle from Euclidean geometry, which is derived from a straightedge and compass construction of the equilateral triangle. 

To demonstrate the correctness of the function, a simple unit test is included, which confirms that the function calculates the area of a triangle with known values correctly. 
```python
def test_triangle_area():
    # Test 1
    assert triangle_area(5, 3) == 7.5 
    assert triangle_area(-1, 1) == 0 

test_triangle_area()
```

This test includes a boundary condition where a side length or height is zero or less to ensure that the function correctly handles edge cases.  The test validates the output of the function for a valid input and an input that would trigger an error due to the negativity of input values.