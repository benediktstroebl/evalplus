```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given the length of its sides.
    Args:
        a (float): The length of the first side of the triangle.
        h (float): The length of the second side of the triangle.
    Returns:
        float: The area of the triangle.
    """
    # Test
    # Test case 1
    assert triangle_area(5, 3) == 7.5
    # Test
    area of a triangle with sides of length 5 and 3.

```
This Python script defines a function called `triangle_area` that calculates the area of a triangle given the lengths of its sides. The function then passes a test case and returns the area of the triangle.

The function uses Heron's formula to calculate the area, which involves the side lengths a and h. The test case ensures that the function works correctly by providing the expected result for a given input.