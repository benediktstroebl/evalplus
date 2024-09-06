```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= a and s >= b and s >= c:
        area = (a * b * s) / 2
        return round(area, 2)
    else:
        return -1
```

The function takes the three side lengths of a triangle as arguments and calculates the semi-perimeter s of the triangle. The semi-perimeter s is computed by summing the three sides and dividing it by two.

Next, the function verifies if the semi-perimeter satisfies the condition for a valid triangle. Valid triangles have the property that the sum of any two sides is greater than the third side.

If the sides form a valid triangle, the function computes the area by applying the formula `area = (a * b * s) / 2`, where a, b, and s are the two sides and the semi-perimeter of the triangle, respectively. Lastly, the function returns the area rounded to two decimal places.

If the sides do not form a valid triangle, the function returns -1 to indicate an invalid triangle. 

This solution adheres to the problem statement and provides the area of a valid triangle, while also handling invalid cases correctly.