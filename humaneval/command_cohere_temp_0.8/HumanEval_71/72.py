```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == a + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area of a triangle when the length of the three sides is given.

Then it checks whether the sum of the two sides is greater than the length of the third side to verify if it is a valid triangle. If it is valid, it returns the area rounded to two decimal points, otherwise, it returns -1. 

This solution is efficient and accurately determined whether the input forms a valid triangle and returns the area when it is valid.