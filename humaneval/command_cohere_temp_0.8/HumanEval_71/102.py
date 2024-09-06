```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(s) * (s - max(s))) / 2
        return round(area, 2)
    else:
        return -1
```

The function first checks whether the sum of the sides is equal to the longest side with some tolerance. If so, it proceeds to calculate the area and round it to two decimal places, returning the result. If the sum does not meet these conditions, the function returns -1. 

This solution utilizes a basic application of the triangle area formula 'base * height / 2' and checks for triangle validity with the 'triangle inequality' rule. 

Such a solution could be improved further in terms of precision and robustness through the introduction of more precise validation checks and by handling edge cases.