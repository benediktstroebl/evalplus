```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * a * c)))), 2)
```
The script uses the sine rule for triangle solution to determine the area of the triangle if the sum of any two sides is greater than the third side, and returns -1 otherwise. To get the precise value for the acos function, the decimal should be set to a higher precision, like '15' for this function.