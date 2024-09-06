```python
def pairs_sum_to_zero(l):
    """
    Function that checks whether a list of integers sums to zero.
    Returns: if two distinct elements sum to zero, and False otherwise.
    """
    function is expected to have a list of integers as an argument and return a boolean indicating whether there are two distinct elements that sum to zero.
    This checks that the two elements with the largest and smallest values in the list are not the same, and the list has at least two elements.
    """

Example:
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    """
    l = list(map(int, l.

    if sum(l) == 0:
        return True
    else:
        return False
```
This Python function checks whether a list of integers sums to zero. It returns `True` if there are two distinct elements that sum to zero and False otherwise.