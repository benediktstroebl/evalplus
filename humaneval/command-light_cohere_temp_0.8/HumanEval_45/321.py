```python
def triangle_area(a, h):
    return 3.14159 * (a ** (h ** 0.5)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.14159 * (5 ** (3 ** 0.5)), "Pass is a valid area"
    assert triangle_area(10, 5) == 220.142940, "Passes the test with a random triangle area"
```