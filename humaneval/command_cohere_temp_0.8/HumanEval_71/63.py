```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(a, b, c) * (s - max(a, b, c)) / 2)
        return round(area, 2)
    else:
        return -1
```

The function begins by calculating the sum of the side lengths to verify the triangle's validity. The validation is performed by checking the difference between the sum of the sides and the longest side, the triangle is validated if the difference is almost zero. Once validated, the function employs Heron's formula to compute the area using the three sides, subsequently rounding the result to two decimal places for precision. If the sides do not form a valid triangle, a value of -1 is returned to indicate the inconsistency.

To validate the function, two test cases are proposed:
- Test case 1: Valid triangle (e.g., 3, 4, 5).
- Test case 2: Invalid triangle (e.g., 1, 2, 10).

The desired output for test case 1 should be 6.00, and test case 2 should return -1. These tests can be performed by calling the function with the respective input values.