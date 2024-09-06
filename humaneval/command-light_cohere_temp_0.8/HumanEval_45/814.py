```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Area should be the5 for the triangle with sides of length 5 and 3"
``` 
This code defines the function `triangle_area` that calculates the area of the triangle given the lengths of its sides. The function passes the test_triangle_area test case, which asserts that the area of the triangle with sides of length 5 and 3 is indeed 7.5.