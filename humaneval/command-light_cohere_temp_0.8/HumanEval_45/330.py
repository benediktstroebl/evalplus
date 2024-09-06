```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** (1/2)

if __name__ == "__main__":
    a = 5
    h = 3
    assert triangle_area(a, h) == 7.5
    print("This is correct!")
```