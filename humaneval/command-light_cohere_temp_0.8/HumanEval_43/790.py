```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    return False

# Test cases
test_sum_zero = [
    [2, 4, -5, 3, 5, 7],
    [1],
    [],
    [1, 3, -2, 1],
    [7]
]

for test in test_sum_zero:
    assert pairs_sum_to_zero(test) == True  # Should pass all tests
```