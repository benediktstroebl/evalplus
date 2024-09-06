```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(a, b, c) * (s - max(a, b, c)) / 2)
        return round(area, 2)
    else:
        return -1
```

The function first checks whether the sum of the sides is equal to the longest side within a threshold. If so, it employs the Heron's formula to calculate the area of the triangle and rounds the result to two decimal places. If not, it returns -1 to indicate that the sides do not form a valid triangle. 

This approach allows the function to determine the triangle's area if the sum of any two of its sides is larger than the third side, which is the condition for a valid triangle.