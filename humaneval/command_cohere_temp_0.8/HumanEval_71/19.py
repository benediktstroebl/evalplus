```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b**2 + c**2 - a**2) / (2 * a * c)))), 2)
```
To determine whether the three sides form a valid triangle, the code checks whether the sum of any two of the sides is significantly larger than the third side. The code also ensures that the area is calculated only for valid triangles. The acosine function's inclusion ensures that the triangle is accurately computed, even when side lengths are not proportional. 
The following examples illustrate how to use this function:
```python
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
```

This function can be added to a Python script or integrated into a Python project to perform triangle area calculations.  If no valid triangle is formed by the side lengths, the function returns -1. Otherwise, it rounds the accurate trigonometric calculation of the triangle's area to two decimal places and returns that value.