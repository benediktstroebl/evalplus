```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 22.28
    assert triangle_area(10, 7) == 98.91
    ```
``` 
This code defines the function `triangle_area` that calculates the area of the triangle using the formula `