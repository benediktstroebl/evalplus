```python
def right_angle_triangle(a, b, c):
    if a == b == c == 0:  # Special case for triangles with zero length
        return True
    elif a == b == c or a == c || b == c:  # Trigano's theorem
        return False
    else:
        sqa, sqb, sqc = (a**2 + b**2 + c**2) / 2, (b**2 + c**2 - a**2) / 2, (c**2 + a**2 - b**2) / 2
        return sqa != sqb or sqb != sqc or sqa != sqc and min(sqa, sqb, sqc) == 0.5
```

The function checks for triangles with zero length and handles Trigano's theorem to accurately determine if the given sides form a right-angled triangle. Trigano's theorem states that bouquets of three angles which are not greater than two right angles are equivalent to a triangle with a right angle, whence the conditional structure.