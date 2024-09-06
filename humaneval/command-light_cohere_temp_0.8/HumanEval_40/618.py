```python
def triples_sum_to_zero(l):
    if set(l) == {0}:
        return True
    return False

# Tests
test_passes = [
    [triples_sum_to_zero([1, 3, 5])], True),
    [triples_sum_to_zero([1, 2, 3])], False),
    [triples_sum_to_zero([2, 4, -5])], True),
    [triples_sum_to_zero([1])], False],
]

for test in test_passes:
    assert triples_sum_to_zero(test) == test[1]
```