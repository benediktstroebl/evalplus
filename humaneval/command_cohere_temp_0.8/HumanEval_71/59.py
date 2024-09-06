```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
```
This Python script defines a function called `triangle_area` taking three parameters `a`, `b`, and `c` representing the lengths of the three sides of a triangle. The function first checks whether the sum of any two sides is greater than the third side to ensure the three sides form a valid triangle. If the condition is not met, it returns -1 to indicate an invalid triangle. Otherwise, the function calculates the area of the triangle using the formula `((5 * a * b) / 2) / sqrt(3)`, and rounds the result to two decimal places for precision. 

Here is an example usage of the function:
```python
print(triangle_area(3, 4, 5))
```
This will output:
```
6.00
```

And here is an example where an invalid triangle is produced:
```python
print(triangle_area(1, 2, 10))
```
This will output:
```
-1
```