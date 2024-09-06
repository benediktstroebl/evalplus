```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```
This Python script defines a function called `triangle_area` taking three parameters `a`, `b`, and `c` as the lengths of the three sides of a triangle. 

The function first calculates the semi-perimeter of the triangle `s = (a + b + c) / 2` and if the semi-perimeter is less than or equal to the maximum of the three sides, it proceeds to calculate the area of the triangle using the Heronian formula `Area = 0.5 * s * (s - a) * (s - b) * (s - c)`. This formula is derived from the fact that the area of a triangle is equal to one-half of the product of its semi-perimeter and any one of its sides. The result is then rounded to 2 decimal places and returned. 

If the semi-perimeter is greater than the maximum of the three sides, it is not a valid triangle, so the function returns -1. 

This approach ensures that the function handles both valid and invalid triangles correctly according to the problem statement.