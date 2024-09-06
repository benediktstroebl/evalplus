```python
def triangle_area(a, h):
    """Return the area of a triangle given a side length and height.
    Uses Heron's formula."""
    s = (a**2 + h**2) / 2
    area = sqrt(s * (s - a**2) * (s - h**2)) / 2
    return area
```

To define the function, I used Heron's formula to calculate the area of the triangle which is `sqrt(s * (s-a)(s-h))` where s is the semi-perimeter of the triangle and a and h are its sides. The semi-perimeter is defined as `s = (a**2 + h**2)/2` and simplifies the formula.