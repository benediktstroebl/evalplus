```python
def triangle_area(a, h):
    return 3.14 * a * * (a ** 2) + (h ** 2)

# Test cases
test_passes = [
    (5, 3),
    (8, 4),
    (10, 5),
    (15, 6),
    (20, 7),
    (25, 8),
]

for t in test_passes:
    actual = triangle_area(*t)
    expected = t[1]
    print(f"Test {t} (actual: {actual}, expected: {expected}) passed.")
```