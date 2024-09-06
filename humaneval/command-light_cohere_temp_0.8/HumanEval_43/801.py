```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Test the function
for _ in range(6):
    assert pairs_sum_to_zero([1, 3, 5, 0]), "Should return False"
    assert pairs_sum_to_zero([1, 3, -2, 1]), "Should return False"
    assert pairs_sum_to_zero([1, 2, 3, 7]), "Should return False"
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), "Should return True"
    assert pairs_sum_to_zero([1]), "Should return False"
```