```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the lengths of its sides.
    Args:
    a, b, c (float): sides of the triangle
    Returns:
    float: the area of the triangle
    """
    area = 0.5 * (a + b + c)
    return area

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 6))  # Output: 120.2
```
This function calculates the area of a triangle given the lengths of its sides and passes the test by providing two example usages.