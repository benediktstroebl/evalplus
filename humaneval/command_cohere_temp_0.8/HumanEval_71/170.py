```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == a + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area of a triangle when the length of any two sides and the hypotenuse is known.

To validate that the lengths of the three sides form a valid triangle, the sum of any two sides is compared to the length of the third side. If the condition is met, the function calculates the area, rounds it to two decimal places, and returns the area. If the condition is not met, the function returns -1 to indicate that a valid triangle cannot be formed with those side lengths. 

This approach ensures that the function handles edge cases and follows the problem statement's guidelines to determine valid triangles and calculate their areas.