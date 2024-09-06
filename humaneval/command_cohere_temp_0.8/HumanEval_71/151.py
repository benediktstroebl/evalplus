```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function `triangle_area` calculates the semi-perimeter of the triangle, defined as the sum of the sides divided by two, and then checks if the semi-perimeter is greater than the largest side. If it is, the function calculates the area of the triangle and returns it rounded to two decimal places. If the semi-perimeter is not greater than the largest side, the function returns -1 to indicate that the sides do not form a valid triangle.

Here is an example usage of the function:
```python
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
```

This demonstrates the function's ability to correctly determine the area of a valid triangle and identify cases where the sides do not form a triangle.