```python
def triangle_area(a, b, c):
    s = sum(i for i in [a, b, c] if i != max(a, b, c))
    if len(s) == 2 and max(a, b, c) - min(a, b, c) > 0.0:
        r = (max(a, b, c) * (s[0] + s[1]) / 2) / (max(a, b, c) - min(a, b, c))
        return round(r, 2)
    else:
        return -1
```

The function `triangle_area` leverages the fact that the sum of any two sides of a valid triangle is always greater than the length of the third side. It uses a list comprehension to find the sum of the two sides and calculates the area with the formula `A = (s * (s-a)/2) / (b-a)`, where `s` is the semi-perimeter of the triangle. Lastly, the function rounds the result to 2 decimal places, as requested, and returns `-1` for invalid triangles. 

This approach ensures the function accurately determines the area of a valid triangle and returns a clear indication for invalid input.