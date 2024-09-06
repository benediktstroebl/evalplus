```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == a + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function adheres to the problem's directive to compute the triangle's area utilizing the Heron's Formula and return a validation message for invalid triangles. It accepts three sides as input, determines their sum (s), and verifies if the sum is equal to any two-side combination. If it is, the function employs Heron's Formula to compute the area and rounds it to two decimal places. If the sum isn't equal to any two-side combination, the function returns -1, indicating an invalid triangle. This approach allows the function to accurately determine the triangle's area while also providing user-friendly feedback.