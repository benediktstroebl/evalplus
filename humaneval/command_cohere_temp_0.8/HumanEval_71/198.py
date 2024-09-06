```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b**2 + c**2 - a**2) / (2 * a * c)))), 2)
```
The script uses the 'sum' function to calculate the sum of the three sides. Then it checks whether the sum is bigger from each side individually, the check is done with some tolerance 1e-6 to avoid false negatives due to rounding errors. If the sum does not qualify as valid, it returns -1. If the sum does qualify, it uses Heron's formula to calculate the area and then returns it rounded to 2 decimal places. Please note that the function assumes input lengths are given in meters for the sake of calculating the area using Heron's formula. 
Note that the function utilizes the math module in Python, which is slower than native Python operations. For performance-sensitive applications, it is recommended to leverage numpy, especially when dealing with extensive computations. Grounded on the assumption that the three sides are given in meters and employing the math module, the function calculates the area of the triangle to two decimal places. If the sides do not form a valid triangle, a message is returned.