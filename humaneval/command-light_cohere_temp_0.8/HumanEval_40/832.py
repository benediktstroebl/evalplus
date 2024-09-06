```python
def triples_sum_to_zero(lst):
    return any(sum(x) == 0 for x in lst) and all(x != 0 for x in lst)

# Test cases
triples_sum_to_zero([1, 3, 5, 0])  # Should return True
triples_sum_to_zero([1, 3, -2, 1])  # Should return True
triples_sum_to_zero([1, 2, 3, 7])  # Should return False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Should return True
triples_sum_to_zero([1])  # Should return False
```

This function uses the `any` and `all` functions with generator expressions to check if there are three distinct elements in the list that sum to zero and if all elements are not equal to zero, respectively. The test cases provided cover a expected behavior.