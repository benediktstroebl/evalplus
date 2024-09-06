```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return '{:.2f}'.format(area)
    else:
        return -1
```

The function `triangle_area` calculates the semi-perimeter of the triangle, defined as the sum of the sides divided by two, and then checks if the semi-perimeter is less than or equal to the longest side. 

If the inequality holds, the function calculates the area of the triangle using Heron's formula and returns it rounded to two decimal places. In the case where the inequality does not hold, the function returns `-1` to indicate that the sides do not form a valid triangle. 

The test cases ensure that the function behaves as expected for both valid and invalid triangles.