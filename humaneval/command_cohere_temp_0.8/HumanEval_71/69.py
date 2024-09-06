```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(x + y for x, y in zip(a, b, c)))>1 and max(a, b, c) <= s / 2:
        return round(0.5 * (s * (s-a) * (s-b) * (s-c))**0.5, 2)
    else:
        return -1
```

The function checks whether the sum of any two sides is greater than the third side and whether the lengths of all three sides are different. If the conditions are met, it calculates the area and returns it rounded to two decimal places, otherwise it returns -1.