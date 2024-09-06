```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b**2 + c**2 - a**2) / (2 * a * c)))), 2)
```

The function checks whether the sum of any two sides is greater than the third side. If the triangle is valid, it calculates the area using the law of cosines. The test cases would look like:
```python
test_cases = [[3, 4, 5], [1, 2, 10], [0, 0, 0], [7, 11, 0], [5, 16, 10], [8, 15, 13]]
for i in test_cases:
    assert triangle_area(*i) == 6 if i[0] + i[1] > i[2] else -1
```