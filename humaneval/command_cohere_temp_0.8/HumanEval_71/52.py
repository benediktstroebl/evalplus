```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        area = (a * b * (s[0] + s[1] + s[2]) / 2) / (s[0] * s[1] + s[1] * s[2] + s[0] * s[2])
        return round(area, 2)
    else:
        return -1
```

The function assesses the validity of the sides provided based on the triangle inequality theorem. If the sum of any two sides is greater than the third, the function calculates the area using the provided formula and rounds the result to two decimal places. Otherwise, it returns -1 to indicate an invalid triangle.