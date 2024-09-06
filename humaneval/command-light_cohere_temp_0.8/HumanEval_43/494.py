```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Test the function
for _ in range(0, 5):
    actual = [1, 3, -2, 1] + [1]
    expected = [False] * 5
    assert pairs_sum_to_zero(actual) == expected, "Test failed!"
```