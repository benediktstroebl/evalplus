```python
def triangle_area(a, h):
    return 5 * a * (h + a) ** 2

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 44.0
    assert triangle_area(10, 5) == 65.2
```
This code defines a function called `triangle_area` that calculates the area of a triangle given the lengths of its sides. It also defines a test function that checks the correctness of the `triangle_area` function with a set of test cases.