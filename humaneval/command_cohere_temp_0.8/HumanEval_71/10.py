```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The provided code defines a Python function called `triangle_area` that estimates the area of a triangle when given its three side lengths as arguments. It first sums the three side lengths and checks if the sum is significantly different from each side length. If any of these differences are greater than a negligible threshold, the function assumes the sides cannot form a valid triangle and returns -1 to indicate this. If the sides can form a valid triangle, the function employs Heron's formula to calculate the area using the three sides, then rounds the result to two decimal places, and returns the rounded value as the estimated area of the triangle.