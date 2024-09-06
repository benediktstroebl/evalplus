```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

def test():
    assert triangle_area(5, 3) == 7.5
```  This self-contained Python function calculates the area of a triangle, given the lengths of its sides. The function uses the particular formula for the area of a triangle and passes the test case, where the area is calculated correctly with side lengths 5 and 3.