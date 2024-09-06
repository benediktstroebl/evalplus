```python
def triangle_area(a, h):
    return 3.14 * a *a * (h + a) ** 2

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 6) == 92
    assert triangle_area(7, 10) == 193
    assert triangle_area(15, 20) == 366
```