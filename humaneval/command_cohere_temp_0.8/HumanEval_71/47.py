```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)) / (12 * s), 2)
```
The given Python script defines a function called `triangle_area` that takes three side lengths as input. It first checks whether the sum of the three sides is equal to the sum of any two other sides, which is a condition for the sides to form a valid triangle. If the conditions are met, it calculates the area of the triangle using the Heronian formula and rounds it to two decimal places. If the sides do not form a valid triangle, the function returns -1.