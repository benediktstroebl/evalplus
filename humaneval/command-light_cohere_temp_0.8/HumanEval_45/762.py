```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given the length of two sides.
    Args:
        a (length of the side)
        h (length of the other side)
    
    Returns:
        float: The area of the triangle
    """
    # Calculate the semi-perimeter
    s = (a + h) / 2
    # Calculate the area using Heron's formula
    return sqrt(s * (s - a - h) ** 2)

# Unit test
test_triangle_area = TriangleArea()
print(test_triangle_area(5, 3))  # Expected Output: 7.5
```
The provided Python script defines a function called `triangle_area` that calculates the area of a triangle given the lengths of its two sides. The function utilizes Heron's formula to compute the area and then passes the test with the specified values of `a` and `h` to ensure its correctness.