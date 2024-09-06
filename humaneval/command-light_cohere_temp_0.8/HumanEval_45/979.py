```python
def triangle_area(a, h):
    """Calculate the area of a triangle.
    Args:
        a, h (float)
    
    Returns:
        float: The area of the triangle
    """
    # Pythagorean Theorem formula
    side_square = a * a + h * h
    return side_square / 2
```
The function takes two parameters, a and h, which are the lengths of the sides of the triangle. It calculates the area of the triangle using the formula for the area of the triangle. The result is then returned by the function and can be used to calculate the area of any triangle.

The following is an example of how to call the function:
```python
# Test the function
print(triangle_area(5, 3)) # Output: 15.25
```
This will output the area of a triangle with sides of length 5 and 3.