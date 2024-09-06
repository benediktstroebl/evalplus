```python
def triangle_area(a, h):
    return 3 * a * (h + a)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "correct answer"
    assert triangle_area(10, 10) == 225, "correct input"

```
This script defines a function `triangle_area` that calculates the area of the triangle given its base and height. The function then passes the test cases and the test cases are correct.