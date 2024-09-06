```python
def pairs_sum_to_zero(l):
    """
    Function to check if list of integers has two distinct elements that sum to zero.
    Return True if the AND False otherwise.
    """
If the list has any negative number, return False.
    """
Test cases:
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
    """
    for num in l:
        if num < 0:
            return False
    return True
```