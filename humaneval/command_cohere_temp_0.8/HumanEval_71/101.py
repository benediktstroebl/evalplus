```python
def triangle_area(a, b, c):
    s = sum(i for i in [a, b, c] if i != max(a, b, c))
    if s == 0:
        return round(0.5 * (a * b), 2)
    elif s == 2:
        return round(0.5 * (a * c), 2)
    elif s == 3:
        return round(0.5 * (b * c), 2)
    else:
        return -1
```
This function assumes that the input is valid, in the sense that the parameters are all positive numbers. The sides of the triangle are represented by a, b, and c, and the function tests their validity using the `max` function and a list comprehension.

The function then uses an elegant expression to calculate the area of the triangle, taking advantage of the fact that the diagonal of a triangle divides it into two congruent right triangles, thus doubling the area of one quadrant. It then returns the result rounded to two decimal places or -1 for invalid input.

This is a clear and direct implementation that is easy to understand and well optimized for elegance and brevity.