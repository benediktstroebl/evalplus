```python
def triangle_area(a, h):
    return 3.14 * a * (a ** 2) + h ** 2  # Using Heron's formula

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.5
    assert triangle_area(8, 5) == 20.0
    ```
```
This code defines a function called `triangle_area` that calculates the area of the triangle with the given sides. The `test_triangle_area` function is used to run the function and check the result against the test cases.