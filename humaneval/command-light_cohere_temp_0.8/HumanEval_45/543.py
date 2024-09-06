```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test"
``` 
This code defines a function called `triangle_area` that calculates the area of a triangle given the lengths of its sides. The function is then passed to the `test_triangle_area` function, which asserts that the function correctly computes the area of a triangle with given sides.