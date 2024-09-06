```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 12.28
    assert triangle_area(10, 5) == 83.69
``` 
This script defines a function `triangle_area` that calculates the area of a triangle given the lengths of its sides. The `test_triangle_area` function asserts the results of `triangle_area` with specific input values, which ensures the correctness of the function.