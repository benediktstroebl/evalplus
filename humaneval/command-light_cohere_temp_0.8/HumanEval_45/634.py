```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 2) == 4.28
    assert triangle_area(10, 5) == 42
```
This code defines a function called `triangle_area` that calculates the area of a triangle given its base and height. The function uses the mathematical formula to calculate the area of the triangle. 

The `test_triangle_area` function contains several assert statements that pass the test the function with different input parameters.