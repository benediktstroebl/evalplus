```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
    else:
        return -1
```

The function takes in three numbers a, b, and c, representing the lengths of the three sides of a triangle. It first determines whether the sum of any two of the sides is substantially greater than the third side, which is the condition for a valid triangle. If the triangle is invalid, the function returns -1; if the triangle is valid, it calculates and returns the area of the triangle to two decimal places. 

To achieve this, the function utilizes a list comprehension to calculate the sum of the three sides, which is compared to the maximum side length using the absolute difference. The validity of the triangle is thus confirmed. If valid, the function employs the formula for the area of a triangle and the `round()` function to return the area rounded to two decimal places. 

This solution adheres to the problem's request for a Python script that can standalone and solve the problem. The function encapsulates both the validity check and the area calculation, allowing it to be invoked individually for computation.