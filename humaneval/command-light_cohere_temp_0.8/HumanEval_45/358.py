```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test case"
    assert triangle_area(3, 3) == 3.8, "Passed test case 2"
    assert triangle_area(10, 5) == 55, "Passed test case 3"

# Sample output:
test_triangle_area()
```