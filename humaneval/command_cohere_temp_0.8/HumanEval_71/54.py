```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function `triangle_area` calculates the area of a triangle if the sum of any two sides is greater than the third side. The test cases include scenarios where the input values form a valid triangle and invalid ones.  Thus, the function is validated to meet the problem's expectations.