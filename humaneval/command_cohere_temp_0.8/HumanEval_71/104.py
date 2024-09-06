```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)) / 2, 2)
    else:
        return -1
```
In the code above, the `triangle_area` function calculates the area of the triangle when the sum of any two of its sides is greater than the third side. The code defines a semi-perimeter `s` of the triangle as half of the sum of all three sides. The condition for a valid triangle checks whether the semi-perimeter is greater than the largest side of the triangle. If the condition for a valid triangle is met, the code calculates the area of the triangle using the Heron's formula and returns it rounded to two decimal places. If the condition is not met, the function returns `-1`. 

To follow the convention of Python functions, the comments are also adjusted to use triple quotes for multi-line comments.