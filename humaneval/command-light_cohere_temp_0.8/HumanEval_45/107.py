```python
def triangle_area(a, h):
    return 3.14159 * (h** 2 * a)

if __name__ == "__main__":
    a = 5
    h = 3
    result = triangle_area(a, h)
    assert result == 7.5
    print("Result is", result)
```