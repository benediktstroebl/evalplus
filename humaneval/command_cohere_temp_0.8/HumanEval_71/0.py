```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The provided code defines a Python function called triangle_area that calculates the area of a triangle when given the lengths of its three sides (a, b, and c). It first checks whether the sum of any two of the side lengths is greater than the third side length. If the condition for a valid triangle is not met, it returns -1 to indicate an invalid triangle. Otherwise, it employs the Heron's formula to calculate the area using the side lengths, and then rounds the result to two decimal places for precision.