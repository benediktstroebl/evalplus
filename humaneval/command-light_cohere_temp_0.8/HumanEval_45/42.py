```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.6
    assert triangle_area(7, 5) == 35.3
```

In this script, the function `triangle_area` calculates the area of a triangle with given side lengths. The `test_triangle_area` function contains test cases that verify the correctness of the `triangle_area` function. 

You can use this script to solve the problem and verify the results with the test cases.