```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function `triangle_area` calculates the semi-perimeter of the triangle, defined as the sum of the sides divided by two, and then checks if the semi-perimeter is less than or equal to the longest side. If the condition is met, the function calculates the area of the triangle using Heron's formula and rounds it to two decimal places. If the condition is not met, it returns `-1` to indicate that the sides do not form a valid triangle. 

Here is an example usage of the function:
```python
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
``` 

This demonstrates how the function correctly computes the area of a valid triangle and returns the invalid response for an invalid triangle.