```python
def triples_sum_to_zero(lst):
    if sum(map(lambda x: x, lst)) < 0:
        return True
    else:
        return False

# Test the function
triples_sum_to_zero([1, 3, 5, 0])  # Should return True
triples_sum_to_zero([1, 3, -2, 1])  # Should return True
triples_sum_to_zero([1, 2, 3, 7])  # Should return False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Should return True
triples_sum_to_zero([1])  # Should return False
```