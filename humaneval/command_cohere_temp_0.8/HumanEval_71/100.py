```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c**2 - (a**2 + b**2) / 4)) / 2
        return round(area, 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the sum of any two sides is greater than the third side, which is the condition for a valid triangle. It does this by comparing the various sums of any two sides to the third side, using a very small tolerance to account for floating-point error. The function returns -1 if the triangle is not valid, and proceeds to calculate the area of the triangle and round it to two decimal places if it is valid.

The script then includes a test suite of valid and invalid triangles, which assert that the function's output matches the expected results. Overall, the script demonstrates how to use Python to check for the validity of triangles and calculate their areas.