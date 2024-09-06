```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 62.5
    assert triangle_area(12, 13) == 85.11
```