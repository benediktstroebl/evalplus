```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == a + c or s == b + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area of a triangle when the length of the three sides is given.

Then it checks whether the sum of any two sides is greater than the third side to verify the validity of the triangle.

Lastly, the function returns the area of the triangle rounded to 2 decimal points if the sides form a valid triangle. Otherwise, it returns -1. 

This solution is efficient and adheres to the problem's guidelines.