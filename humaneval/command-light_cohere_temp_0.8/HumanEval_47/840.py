```python
def median(l: list):
    n = len(l)
    m = n // 2 + 1
    if n % 2 == 0:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]

# Test cases
tests = [
    [(-10, 4, 6, 1000, 10, 20),
     (2, 3, 6, 7, 8, 9, 10),
     (10, 100, 200, 0, -20),
     (-20, 0, -20, -200, -100, -200)]
]

for case in tests:
    got = median(case)
    assert got == case[1]
```