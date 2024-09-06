```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= a and s >= b and s >= c:
        area = (a * b * sin(180 / 3 - arcsin(s / a))
                + b * c * sin(180 / 3 - arcsin(s / b))
                + c * a * sin(180 / 3 - arcsin(s / c)))
        return round(area, 2)
    else:
        return -1
```

The function `triangle_area` calculates the area of a triangle when given the lengths of its three sides. It does this by first calculating the semi-perimeter s, which is half of the sum of the side lengths.

Next, the function checks if the sides form a valid triangle by comparing the semi-perimeter s with each of the side lengths individually. If s is greater than or equal to each individual side length, then the sides do form a valid triangle, and the function proceeds with the area calculation.

The formula for the area of a triangle given its side lengths a, b, and c is derived from Heron's formula. The function directly computes this area using trigonometric functions and the semi-perimeter s.

If the sides do not form a valid triangle (when the semi-perimeter is smaller than at least one of the side lengths), the function returns -1.

The function then rounds the computed area to 2 decimal places for readability and returns it.