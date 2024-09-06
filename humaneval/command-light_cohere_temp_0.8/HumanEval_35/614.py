```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    [(5, 5)],
    ([3, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9],),
    ([10, 9, 8, 7, 6, 5],),
]

for t, expected in test_max_element:
    actual = max_element(t)
    print(f"Test {t}: {actual}, expected={expected}")
```