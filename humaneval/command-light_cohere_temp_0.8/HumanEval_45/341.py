```python
def triangle_area(a, h):
    return 3.14159 * (a **h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Should return the same area for triangle with sides 5 and 3"

print("Testing triangle_area function:")
test_triangle_area()
```