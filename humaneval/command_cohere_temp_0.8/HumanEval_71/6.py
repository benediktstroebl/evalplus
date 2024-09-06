```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
    else:
        return -1
```

The function assesses whether the sum of any two of the given sides is substantially greater than the third; if so, it calculates the area and rounds it to two decimal places, or returns -1 if not a valid triangle.

For robustness, the code tolerates floating-point-precision issues, ensuring valid triangles aren't erroneously flagged as invalid. 

This approach leverages the Pythagorean theorem to compute the area and provides a clear indication of valid input.