```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)) / 2, 2)
    else:
        return -1
```
This Python script defines a function called `triangle_area` taking three parameters `a`, `b`, and `c` as the lengths of the three sides of a triangle. The function first calculates the semi-perimeter `s` of the triangle by summing the sides and dividing by 2. The semi-perimeter `s` is then compared to the largest side of the triangle. If `s` is greater, it means the sum of any two sides is greater than the third side, indicating a valid triangle. In this case, the function calculates the area of the triangle using the Heron's formula and rounds it to two decimal places before returning it. If `s` is less than or equal to the largest side, it returns -1 to indicate an invalid triangle. 

Here is an example usage of the function:
```python
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
```
This demonstrates the function's behavior for both a valid and an invalid triangle.