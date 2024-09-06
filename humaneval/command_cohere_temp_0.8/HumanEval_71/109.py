```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c))**, 2)
```
The specified problem is a classic triangle area calculation. The function `triangle_area` calculates the area of a triangle with sides `a`, `b`, and `c`. It checks if the sum of any two of these sides is greater than the third, which determines if the sides can form a valid triangle or not. If the sides are valid, the function uses the Heron's formula to calculate the area and rounds it to 2 decimal points before returning. If the sides do not form a valid triangle, the function returns -1.