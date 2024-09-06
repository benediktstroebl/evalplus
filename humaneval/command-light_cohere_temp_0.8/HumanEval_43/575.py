```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
list of integers should be sorted in ascending before passing it to this function.
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    """
    if sum(sorted(l)) == 0:
        return True
    else:
        return False
```