```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

if __name__ == "__main__":
    a = float(5)
    h = float(3)
    assert triangle_area(a, h) == 7.5
    print("Passed test case!")
```