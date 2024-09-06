```python
def triangle_area(a, h):
    """ Calculate the area of the triangle. area of a triangle using the formula.
    return (a * (h)) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.25, "Passed test"
    assert triangle_area(10, 5) == 50, "Failed test"
    assert triangle_area(4, 8) == 20, "Failed test"

``` 
This code defines a `triangle_area` function that calculates the area of a triangle using the formula (a * h) / 2. It also includes a test_triangle_area function to test the correctness of the `triangle_area` function.