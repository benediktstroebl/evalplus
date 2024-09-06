```python
def triples_sum_to_zero(lst):
    if sum(map(sum, lst)) == 0:
        return True
    else:
        return False

# Test cases
triples_sum_to_zero([1, 3, 5, 0])  # Should return True
triples_sum_to_zero([1, 3, -2, 1])  # Should return True
triples_sum_to_zero([1, 2, 3, 7])  # Should return False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Should return True
triples_sum_to_zero([1])  # Should return False
```
This function is straightforward and easy to understand. It checks if the sum of all elements in the list is equal to zero, which indicates that there are three distinct elements whose sum equals zero.