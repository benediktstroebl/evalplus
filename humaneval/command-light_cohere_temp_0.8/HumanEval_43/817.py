```python
def pairs_sum_to_zero(l):
    return any([x + y = 0 for x, y in zip(l, l[1:])])

# Tests
test_pairs_sum_to_zero = [
    ([1, 3],),
    ([1, 2, 3, 7],),
    ([2, 4, -5, 3, 5, 7],),
    ([1,]),
]

for test_case in test_pairs_sum_to_zero:
    actual = pairs_sum_to_zero(test_case)
    assert actual == False, f"Expected False, but got {actual}"
```