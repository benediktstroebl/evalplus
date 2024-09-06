```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(4, 2) == 6.25
    assert triangle_area(6, 8) == 112.00
``` 
The code defines a function called `triangle_area` that calculates the area of a triangle using the formula (a * (h + a) / 2)). The `test_triangle_area` function contains a series of tests that verify the correctness of the `triangle_area` function with different inputs.