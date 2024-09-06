```python
def median(l):
    """Return median of elements in the list l"""
    return (len(l) + 1) * int((l[-1] + l[0]) / 2)

# Test cases
test_median = [
    [(1, 2, 3), (-10, 4, 6, 1000, 10, 20)],
    ([10, 20, 30], [-100, -200, -1000])
]

for test in test_median:
    actual = median(test)
    expected = sum(map(int, test)) // 2
    assert actual == expected, f"Test {test} failed: actual={actual}, expected={expected}"
```