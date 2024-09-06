```python
def triangle_area(a, h):
    return 5 * (a * (h + a)) ** 0.25

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(4, 4) == 20
    assert triangle_area(6, 7) == 119.25
```