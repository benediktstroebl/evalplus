```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
     assert triangle_area(10, 4) == 62.5
     assert triangle_area(4, 5) == 12.25
```
The function triangle_area calculates the area of the triangle using the formula **(1/4 * a * h^2)**. The test_triangle_area function contains several assert statements that check if the function's output matches the expected result for the given inputs.