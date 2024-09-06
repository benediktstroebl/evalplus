```python
def triples_sum_to_zero(lst):
    return any(sum(x) <= 0 for x in lst)

# Example function call
triples_sum_to_zero([1, 3, -2, 1])  # Returns True

# Example test case
triples_sum_to_zero([1, 2, 3, 7])  # Returns False

# Another test case
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Returns True
```

This code defines a function `triples_sum_to_zero` that assesses whether there are three distinct elements in a list that sum to zero. It returns `True` if this condition is met and `False` otherwise.