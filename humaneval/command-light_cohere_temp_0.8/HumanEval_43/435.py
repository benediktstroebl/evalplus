```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    list of integers is first passed to the function, and it returns
    True if there are two distinct elements in the list that sum to zero,
    False otherwise.
    """
example:
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    True
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i in range(len(l)):
        if l[i] == l[i] + l[i]:
            return False
    return True
```