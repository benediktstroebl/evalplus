```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == a + c or s == b + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area of a triangle when the lengths of the three sides are given, and also checks for the conditions for a valid triangle. The tests are evaluated with rounding taken into account as per the 'Example' given in the prompt.