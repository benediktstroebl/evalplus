```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(4, 4) == 12.0
    assert triangle_area(6, 2) == 12.0

if __name__ == "__main__":
    test()
```