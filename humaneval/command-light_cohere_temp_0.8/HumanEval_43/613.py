```python
def pairs_sum_to_zero(l):
    """
    Function to check whether all elements in the list sum up to zero.
    Returns: True if all elements sum up to zero, and False otherwise.
    """
    Test case:
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    """
    return sum(x for x in l) == 0
```