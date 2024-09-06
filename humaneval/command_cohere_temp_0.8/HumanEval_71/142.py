```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c))**, 2)
```

The function checks whether the sum of any two of the input sides is greater than the third side. If the triangle is valid, it calculates the area and returns it rounded to two decimal places. If the sides form an invalid triangle, it returns -1.