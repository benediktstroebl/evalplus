```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)) / 12, 2)
    else:
        return -1
```
This Python script defines a function called `triangle_area` that takes three arguments: `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first calculates the semi-perimeter of the triangle, which is the sum of any two sides of the triangle divided by 2. The semi-perimeter is then used to determine if the sides form a valid triangle using the triangle inequality theorem. 

If the semi-perimeter is less than or equal to the largest side, the function calculates the area of the triangle using the Heron's formula and returns it rounded to two decimal places. Otherwise, it returns -1 to indicate that the sides do not form a valid triangle. 

This solution adheres to the problem statement by providing the area for a valid triangle and handling cases where the side lengths do not satisfy the triangle inequality.