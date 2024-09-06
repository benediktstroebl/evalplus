```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

if __name__ == "__main__":
    a = 5.0
    h = 3.0
    print("Triangle area:", triangle_area(a, h))
    assert triangle_area(a, h) == 7.5
```