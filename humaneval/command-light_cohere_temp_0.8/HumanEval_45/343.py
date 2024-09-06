```python
def triangle_area(a, h):
    return 3.14159 * (a**2) / 2 - (a**2 + h**2)

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.8
    assert triangle_area(8, 7) == 22.6
    assert triangle_area(10, 5) == 687.92
    print("All calculations passed!")
```