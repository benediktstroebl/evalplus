```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 2) == 19.6
    assert triangle_area(12, 13) == 62.5
``` 
This script defines a function called `triangle_area` that calculates the area of the triangle with given sides. The `test_triangle_area` function contains three assertions that test the function with different inputs and the expected output values.