```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 62.2857
   
 
```
The provided Python script defines a function `triangle_area` that calculates the area of the triangle with given sides using the formula `area = (1/4) * a * (b^2 + h)`. The script also includes a test function `test_triangle_area` that asserts the correctness of the `triangle_area` function with different input values.