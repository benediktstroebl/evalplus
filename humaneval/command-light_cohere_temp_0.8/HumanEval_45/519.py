```python
def triangle_area(a, h):
    return a * (h + triangle_area(a, h)/2) 

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
     assert triangle_area(3, 3) == 3
    
test_triangle_area()
```