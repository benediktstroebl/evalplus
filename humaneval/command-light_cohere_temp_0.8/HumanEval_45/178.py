```python
def triangle_area(a, h):
    return 3.14159 * (a**2 * h)

if __name__ == "__main__":
    a = 5.0
    h = 3.0
    assert triangle_area(a, h) == 7.5
    print("Success! It passes the test!")
```