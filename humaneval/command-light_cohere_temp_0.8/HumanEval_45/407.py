```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 10) == 220
    assert triangle_area(0, 5) == 0
    assert triangle_area(20, 6) == 60
    assert triangle_area(3, 7) == 22.5
``` 
This code defines a function `triangle_area` that calculates the area of a triangle with the given sides `a` and `h`. The `test_triangle_area` function tests the `triangle_area` function by passing in different inputs and asserting the results. 

This code uses the `assert` statement to specify that the test cases are independent and will only be evaluated once.