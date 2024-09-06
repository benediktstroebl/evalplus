```python
def pairs_sum_to_zero(l):
    """
    Check whether all elements in the list sum to zero.
    """
    Returns:
    return True if all(x+y <= 0 for x,y in l), otherwise False.
    """
    return True

# Test cases
>>> pairs_sum_to_zero([1, 3, 5, 0])
False
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
```