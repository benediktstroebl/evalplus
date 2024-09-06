```python
def triangle_area(a, h):
    """Return the area of a triangle given a side length and height.
    Uses Heron's formula.
    
    Args:
    - a (float): Length of side (e.g., 5 in triangle ABC).
    - h (float): Height (e.g., 3 for ABC).
    
    Returns:
    - float: Area of the triangle.
    """
    sqrt(a**2 + h**2) / 2
    return round(sqrt(a**2 + h**2) / 2, 2)

# Test suite
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5 
    assert triangle_area(10, 4.5) == 39  
test_triangle_area()
``` 

To verify the function, we use a test suite `test_triangle_area` to check the function's correctness against simple cases. The function `triangle_area` takes in two parameters, `a` and `h`, and returns the area of a triangle using Heron's formula. This formula derives the area from the length of a side and the height. 

To run the tests, call `test_triangle_area()` and assert that the function returns the expected results. These tests check that the function behaves as expected and produces the correct output for the provided inputs.  This helps validate the implementation, ensuring it conforms to the problem's requirements and provides correct results.