```python
def triangle_area(a, h):
    return 3.14 * a * a * h

def test_triangle_area():
    assert triangle_area(5, 3) == 7.14 * 5 * 3 and 3.5
   

def test_two_sided_triangle():
    assert triangle_area(2, 4) == 6.14
    assert triangle_area(5, 5) == 12.28
    assert triangle_area(8, 10) == 196

# Run the function tests
test_triangle_area()
test_two_sided_triangle()
```