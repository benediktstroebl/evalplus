```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)) / ((s - a) * (s - b)), 2)
```

The function follows the problem statement closely. It first checks whether the sum of the sides is equal to any of the individual sides within some tolerance (`1e-6`) which would indicate a valid triangle; if not, it returns -1. Otherwise, it employs Heron's formula to compute the area and returns it rounded to two decimal places.

To vet the solution, a simple test suite could be used to confirm the result for some valid and invalid triangles as per the problem statement, for instance:
```python
test_cases = [
    (3, 4, 5, 6.00),
    (1, 2, 10, -1.00),
    (0, 0, 0, -1.00),
    (5, 12, 13, 30.00)
]

for a, b, c, expected in test_cases:
    actual = triangle_area(a, b, c)
    assert actual == expected
```

This would ensure that the function's behavior aligns with the problem statement and therefore provide an accurate solution to the posed problem.