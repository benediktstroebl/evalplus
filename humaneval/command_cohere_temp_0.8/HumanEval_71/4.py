```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= a and s >= b and s >= c:
        area = (a * b * math.sin(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the logic of calculating the area of a triangle when the lengths of the three sides are given. It first checks if the sides make a valid triangle by verifying if the semi-perimeter is greater than or equal to each side length. If the conditions are met, it proceeds to calculate the area using the sine formula, accurately computing the angle from the side lengths. The final area is returned rounded to two decimal places. If the sides do not form a valid triangle, the function returns -1, indicating an invalid shape. This approach ensures both accuracy and efficiency in determining the area of a triangle based on side lengths.