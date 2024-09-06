```python
def triples_sum_to_zero(lst):
    return any(sum(x) < 0 for x in lst) and any(x != 0 for x in lst)

# Testing the function with the same test cases as the original script
testing_func = triples_sum_to_zero
testing_func( [1, 3, -2, 1])  # Should return True
testing_func( [1, 2, 3, 7])  # Should return False
testing_func([2, 4, -5, 3, 9, 7])  # Should return True
testing_func([1])  # Should return False
```