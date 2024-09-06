```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 6) == 12.0
    assert triangle_area(7, 8) == 28.2
``` 
This Python code defines a function `triangle_area` that calculates the area of a triangle. The `test_triangle_area` function contains three test assertions that check if the `triangle_area` function correctly computes the area of a triangle with different given side lengths and heights.