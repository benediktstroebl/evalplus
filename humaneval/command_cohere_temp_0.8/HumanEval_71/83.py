```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (a * b * (c ** 2) - b * c * (a ** 2)) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the problem's instructions to first check whether the sum of the sides is equal to the maximum side value with tolerance. Then, the function employs the Heronian formula to calculate the area and returns it rounded to 2 decimal points, or -1 if the sides do not form a valid triangle.

Ensure that the Tolerance value used for comparison is sufficiently small, as floating-point comparisons may exhibit subtle differences in precision across different computing environments. This helps mitigate the likelihood of encountering false positives or negatives. 

This code assumes that the inputs are valid numbers, which the question does not explicitly address. Additional validation to ensure that a, b, and c are all positive numbers could be included for more robust code.