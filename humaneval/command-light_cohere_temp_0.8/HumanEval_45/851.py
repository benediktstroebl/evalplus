```python
def triangle_area(a, h):
    return 3.14 * a * * (a ** 2) / 2 

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 22.14
    assert triangle_area(0, 0) == 0
    assert triangle_area(1, 0) == 0
    assert triangle_area(10, 1) == 11.14
``` 
This code defines a function `triangle_area` that calculates the area of the triangle with the parameters `a` (base) and `h` (height). It also includes several test cases to ensure the correctness of the function.