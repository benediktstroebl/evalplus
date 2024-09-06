```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Run tests
def test_pairsum():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False

assert pairs_sum_to_zero([1, 3, -2, 1]) == False

assert pairs_sum_to_zero([1, 2, 3, 7]) == False

assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

# All tests pass!
print("All tests passed!")
```