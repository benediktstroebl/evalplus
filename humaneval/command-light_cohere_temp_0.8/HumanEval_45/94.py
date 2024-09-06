```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 6) == 10.25
    assert triangle_area(10, 5) == 255.2
    assert triangle_area(8, 10) == 25.28

if __name__ == "__main__":
    test()
```