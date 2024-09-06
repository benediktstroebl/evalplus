```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function takes the three side lengths as arguments and checks if the semi-perimeter s is larger than the longest side. If it is, it calculates the area as described in the prompt; otherwise, it returns -1. To ensure everything is self-contained, the max() function is used which is standard in Python.