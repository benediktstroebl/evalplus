```python
def triangle_area(a, h):
    return 3.14 * (a** / h)

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5, "Failed to calculate area correctly"
    assert triangle_area(8, 4) == 22.0, "Failed to calculate area correctly"
    assert triangle_area(13, 10) == 169.0, "Failed to calculate area correctly"
```

This code defines a function `triangle_area` that calculates the area of the triangle given the base and height of one of its sides. The code then includes a test that verifies if the function is working correctly.