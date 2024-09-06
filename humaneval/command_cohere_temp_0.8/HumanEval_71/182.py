```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
The function first checks if the sum of any two sides is greater than the third side, which defines valid triangles. If the triangle is valid, it uses Heron's formula to calculate the area and rounds the result to two decimal places. If the sides do not form a valid triangle, it returns -1. Please note that this approach assumes the input is valid floating point numbers. Adding additional checks or handling invalid inputs based on the specific use case can improve robustness.