```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the base and height."""
    return 0.5 * (h + a **2) / 2 

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Should return the same value."
``` 
This Python script defines a function `triangle_area` that calculates the area of a triangle given its base and height. The `test_triangle_area` function asserts that the function's output is correct for a given input.