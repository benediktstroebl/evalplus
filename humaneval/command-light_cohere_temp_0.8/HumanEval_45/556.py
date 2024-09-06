```python
def triangle_area(a, h):
    return 3.14 * a * (a**2) / 2

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 22.5
    assert triangle_area(12, 5) == 56.28
    assert triangle_area(15, 10) == 94

```