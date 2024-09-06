Here is a Python script that defines a function triangle_area to calculate the area of the triangle:
```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle.
    Args:
    a (given length of the triangle's side)
    h (given height of the triangle)
    Returns:
    The area of the triangle.
    """
    # Check if the arguments are valid
    if not isinstance(a, (float, int)) or not isinstance(h, (float, int)):
        raise TypeError("Invalid input types. Please provide valid float or Elliot numbers (ints or floats).")
    # Calculate the area of the triangle using the Heron's formula
    area = (a * (a + h) * (h + 1) / 4)
    return area

# Unit test to check the function's functionality
test_area = triangle_area(5, 3)
assert test_area == 7.25
```
The function `triangle_area` calculates the area of a triangle based on the length of its side and the height of the triangle. The function includes input validation to ensure that the provided values are valid floating-point numbers. The test at the area is calculated using the Heron's formula and the result is compared to the expected area of the triangle with the given side length and height.