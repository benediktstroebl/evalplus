```python
def pairs_sum_to_zero(lst):
    """
    Returns True if the list has two distinct elements that sum to zero, 
    and False otherwise.
    """
    Test case:
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for x, y in lst:
        if x + y == 0:
            return True
    return False
```