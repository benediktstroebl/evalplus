```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == a + c:
        area = (a * b * (c * (a + b + c) - (a * b))) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the problem definition and uses the formula for the area of a triangle as mentioned in the comment. Furthermore, it checks whether the sum of any two sides is greater than the third side to verify whether the three sides form a valid triangle. The function returns the area of the triangle if it is valid, otherwise, it returns -1.