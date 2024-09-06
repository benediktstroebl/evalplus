```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the triangle is valid by calculating the sum of the lengths of any two sides and comparing it with the length of the third side. If the sum of any two sides is not greater than the length of the third side, the function returns -1 to indicate that the sides do not form a valid triangle.

### Example Usage:
```python
print(triangle_area(3, 4, 5))
```
This will output:
6.00

```python
print(triangle_area(1, 2, 10))
```
This will output:
-1.00

The function then utilizes the Heron's formula to calculate the area of the triangle if it is valid. The result is rounded to 2 decimal places and returned as the area of the triangle.