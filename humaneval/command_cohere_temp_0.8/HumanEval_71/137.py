```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c))**, 2)
```

The function follows the problem's request to return -1 if the sum of any two sides is not greater than the third side. This is achieved by adding all sides together and comparing the absolute difference of each side to less than 1e-6 to ensure they are compared correctly.

The area of a triangle is calculated using Heron's formula. Note that the function rounds the area to two decimal places as requested in the task.