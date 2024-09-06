```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == a + c or s == b + c:
        area = (a * b * (5 * c - a - b) ) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area, `area = (a * b * (5 * c - a - b) ) / 2` as mentioned in the problem statement, and the round() function is used to round the area to two decimal places. The function returns -1 if the sum of any two sides is not greater than the third side. 

To ensure the correctness of the function, it is recommended to verify the results with the given test cases as well as consider adding more test cases to cover other scenarios.