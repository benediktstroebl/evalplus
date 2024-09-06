```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        try:
            area = (a * b * math.sin(math.pi / 3)) / 2
            return round(area, 2)
        except TypeError:
            return -1
    else:
        return -1
```
The function first checks whether the sum of any two of the sides is greater than the third side. If the sum checks out, the function then calculates the area of the triangle using the given side lengths and returns it rounded to two decimal places. If there is any issue in calculating the area, the function returns -1. This approach ensures the validity of the triangle with validated computations.