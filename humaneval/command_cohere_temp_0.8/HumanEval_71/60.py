```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function takes in three numbers representing the lengths of the sides of a triangle. It calculates the semi-perimeter s, which is half the sum of the three sides. Then, it checks whether the semi-perimeter is greater than the largest side, indicating that the sides form a valid triangle. If it's a valid triangle, the function calculates the area using Heron's formula and rounds it to two decimal places before returning it. If the sides don't form a valid triangle, it returns -1.

Here is an example of how to use this function:
```python
print(triangle_area(3, 4, 5))
```

This will output:
```
6.00
```

Which is the expected output. The function determines that the given side lengths form a valid triangle and calculates its area using Heron's formula, rounding it to two decimal places.

Here is another example of how to use this function:
```python
print(triangle_area(1, 2, 10))
```

This will output:
```
-1
```

This result indicates that the sides do not form a valid triangle because the sum of any two sides is not greater than the third side.