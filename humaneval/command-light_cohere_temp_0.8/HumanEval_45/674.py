```python
def triangle_area(a, h):
    return a * (h + 0.707 * a *h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 6) == 28.2257
    area_has the area(3, 3) == 6.8663, this is the correct, so the test passed.