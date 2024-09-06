```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        ar = (a * b * (c ** 2) - a * c * (b ** 2)) / 2
        return round(ar, 2)
    else:
        return -1
```

The provided code defines a Python function called `triangle_area` that calculates the area of a triangle when given the lengths of its three sides `a`, `b`, and `c`. It first checks whether the sum of any two sides is greater than the third side, which is a condition for the sides to form a valid triangle. If the sides form a valid triangle, it uses the Heron's formula to compute the area and rounds the result to two decimal places before returning it. Otherwise, it returns -1 to indicate that the sides do not form a valid triangle.