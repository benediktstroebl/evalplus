```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Test the function
test_pairsum_to_zero = lambda: pairs_sum_to_zero([1, 3, 5, 0])  # Should return False
test_pairsum_to_zero([1, 3, -2, 1])  # Should return False
test_pairsum_to_zero([1, 2, 3, 7])  # Should return False
test_pairsum_to_zero([2, 4, -5, 3, 5, 7])  # Should return True
test_pairsum_to_zero([1])  # Should return False
```

This code provides a self-contained function that solves the problem of checking if there are two elements in a list that sum up to zero. It also includes a corresponding tests that cover various cases.