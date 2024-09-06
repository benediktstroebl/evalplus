```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= a and s >= b and s >= c:
        area = (a * b * c) / 2
        return round(area, 2)
    else:
        return -1
```
The function `triangle_area` calculates the semi-perimeter of the triangle, defined as the sum of the sides divided by two. The semi-perimeter is then checked against each side length individually to ensure it is greater than or equal to each side. If all conditions are met, the function calculates the area of the triangle using the formula `area = (a*b*c)/2` and rounds it to 2 decimal places before returning it. If the conditions are not met, the function returns -1, indicating an invalid triangle. 
This approach ensures that the function handles both valid and invalid triangles correctly based on the given criteria. Failing any of the side-length comparisons with the semi-perimeter implies that the sides cannot form a valid triangle according to the given conditions, and the function accordingly returns -1.