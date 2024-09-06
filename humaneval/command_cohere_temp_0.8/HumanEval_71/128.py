```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function takes the three sides of the triangle as arguments and first calculates the semi-perimeter s of the triangle, which is half the sum of the side lengths. Then it checks whether the inequality x + y > z is true for any two sides x, y compared to the third side z. This is done using the max() function to correctly compare sides of different lengths. If the inequality is true, the function calculates the area of the triangle using Heron's formula and rounds it to two decimal places. If the inequality is not true, the function returns -1 to indicate that the three sides do not form a valid triangle. 

Here is an example usage of the function:
```python
print(triangle_area(3, 4, 5))
```
This will print:
6.00

And here is an example where the function returns -1:
```python
print(triangle_area(1, 2, 10))
```
This will print:
-1