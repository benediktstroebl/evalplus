```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

if __name__ == "__main__":
    a = 5
    h = 3
    assert triangle_area(a, h) == 7.5
    print("Test passed")
```