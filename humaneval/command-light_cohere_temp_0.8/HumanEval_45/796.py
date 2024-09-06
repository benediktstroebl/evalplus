```python
def triangle_area(a, h):
    return 3.0 * a *a * (h + a)

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 56
    assert triangle_area(10, 12) == 198
```