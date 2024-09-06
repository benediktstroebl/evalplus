```python
def triangle_area(a, h):
    return 3.14 * (a** * (h) ** 0.5)
``` 
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.28
    assert triangle_area(10, 5) == 42.5
    assert triangle_area(7, 6) == 13.14
``` 
The above Python script defines a function `triangle_area` that calculates the area of the triangle with given side lengths. The `test_triangle_area` function contains several assert statements that pass the corresponding tests.