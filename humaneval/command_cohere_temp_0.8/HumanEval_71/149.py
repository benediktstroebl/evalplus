```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-6:
        area = (max(s) * (s - min(s))) / 2
        return round(area, 2)
    else:
        return -1
```

The function begins by computing the sum of the three sides a, b, and c. It then checks whether the difference between the sum and the maximum side value is extremely close to zero. This is a fuzzy comparison that tolerates rounding errors, ensuring that the triangle is considered valid even if the side lengths are floats. The reason for this is to accommodate potential floating-point precision issues.

Should the triangle be valid, the function proceeds to calculate the area using the Heron's Formula. Specifically, it uses the formula `max(s) * (s - min(s)) / 2`, where s is the sum of the side lengths. The result is then rounded to two decimal places for precision.

If the triangle is not valid, the function returns -1 to signify an invalid shape. Such a triangle doesn't qualify as a valid geometric shape, and returning -1 communicates this situation effectively. 

This function covers all the bases, from handling floating-point precision to validating triangles and calculating areas.