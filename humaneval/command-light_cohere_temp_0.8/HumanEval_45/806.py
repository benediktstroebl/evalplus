```python
def triangle_area(a, h):
    return a * (h / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Should return 7.25"
    test_triangle_area(8, 6)

def test_second():
    assert triangle_area(6, 8) == 24, "Should return 24"
``` 
This code defines a function `triangle_area` that calculates the area of the triangle given the base and height. It also has two test functions: `test_triangle_area` to check the function's correctness with the first test case and `test_second` to check the function's correctness with a different set of test cases.