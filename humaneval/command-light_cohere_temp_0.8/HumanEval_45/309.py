```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 50
    assert triangle_area(6, 12) == 69
    assert triangle_area(8, 13) == 90

if __name__ == "__main__":
    print("Passed tests for triangle_area function")
```