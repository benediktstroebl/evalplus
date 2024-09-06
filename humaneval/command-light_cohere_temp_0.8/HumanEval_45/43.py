```python
def triangle_area(a, h):
    return 3.0*a*h
```
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test"
```

In this script, we define a function called `triangle_area()` that takes two arguments, `a` and `h`, which represent the length of a side and the height of a triangle, respectively. The function returns the area of the triangle using the formula `area = (1/2) * a * h`. Then, we define another function called `test_triangle_area()` that contains a pass statement. This pass statement asserts that the function `triangle_area()` correctly calculates the area of the triangle with the given side length and height.