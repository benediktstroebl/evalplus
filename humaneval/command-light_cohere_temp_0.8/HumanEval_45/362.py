```python
def triangle_area(a, h):
    return sqrt(3 * (a**2 + h**2) / 4)

#Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(3, 3) == 3.0
assert triangle_area(10, 5) == 42.0
assert triangle_area(-5, -3) < 0
```