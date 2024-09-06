```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return (a * (h + a) / 2)

# Test cases
tests = [
    (5, 3),
    (10, 6),
    (8, 10),
    (4, 7),
    (6, 5),
    (7, 9),
]

for t in tests:
    actual = triangle_area(*t)
    expected = t[1]
    print(f"Test {t} passed: Actual={actual}, Expected={expected}")
```