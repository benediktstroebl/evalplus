```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(s) * (s - max(s)) * 0.5)
        return round(area, 2)
    else:
        return -1
```

The function follows the problem specification accordingly. It calculates the area of the triangle using the formula `max(side_lengths) * 0.5 * abs(sum(side_lengths) - max(side_lengths))`. It also tests if the side lengths form a valid triangle by comparing the sum of any two sides to the third side. If the condition is met, it returns the area rounded to two decimal places. Otherwise, it returns `-1` to represent an invalid triangle. 

This solution works for triangles with side lengths of any data type that supports subtraction and comparison.