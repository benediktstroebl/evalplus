```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function takes the three side lengths as arguments and checks if the sum of any two of them is greater than the third. If so, it calculates the semi-perimeter and uses Heron's formula to derive the area, rounding it to two decimal places. In all other cases, it returns -1. You can test the function using the examples provided in the original prompt.