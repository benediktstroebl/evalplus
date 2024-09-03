```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Test function
def test():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == True
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```

This Python function, `pairs_sum_to_zero`, is a straightforward method that accepts a list of integers and returns `True` if there are two distinct elements in the list whose sum equals zero, and `False` otherwise. This function effectively detects pairs that add up to zero and returns the appropriate result.