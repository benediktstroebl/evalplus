```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]

# Test cases
test_median = [
    [-10, 4, 6, 1000, 10, 20],
    [1, 2, 3, 4, 5],
    [5, 10, 20, 30, 40, 50],
    [0.5, -5, 6, 7, 8, 9],
]

for case in test_median:
    assert median(case) == case[len(case) // 2], f"Case {case} failed"
```