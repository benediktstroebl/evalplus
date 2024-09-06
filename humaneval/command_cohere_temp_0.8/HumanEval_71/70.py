```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(x + y for x, y in zip(a, b, c)) ) == 2 or (2 * max(a, b, c) >= s and 2 * min(a, b, c) <= s):
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)) / (2 * s), 2)
    else:
        return -1
```

The function checks whether the sum of any two sides is greater than the third side and then uses Heron's formula to calculate the area of the triangle. Two sides are taken from the three provided and compared to the third in a set operation, ensuring the comparison doesn't trigger a triangle inequality violation. If this condition is met, it calculates and returns the area; otherwise, it returns -1. Please ensure you address the missing part *{}* where the logic falters.