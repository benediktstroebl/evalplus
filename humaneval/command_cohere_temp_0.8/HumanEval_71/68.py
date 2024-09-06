```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return '{:.2f}'.format(area)
    else:
        return -1
```

The function follows the formula to calculate the area, and then checks whether the sum of any two sides is greater than the third side to validate the triangle. The output is formatted to round the area to 2 decimal places, or -1 for an invalid triangle. 

To ensure the accuracy of the function, it is recommended to address potential edge cases such as floating-point precision issues or very small side lengths. You can use absolute value checks or double-checking the sides' magnitude to tackle these potential issues.